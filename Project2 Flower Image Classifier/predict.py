import torch
from torchvision import models
from torchvision.transforms import transforms
from PIL import Image
import argparse

def process_image(image_path):
    """Process an image for inference."""
    image = Image.open(image_path)
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    return preprocess(image).unsqueeze(0)

def load_checkpoint(filepath):
    """Load a trained model from a checkpoint."""
    checkpoint = torch.load(filepath)
    model = models.vgg16(weights=None)
    model.classifier = checkpoint['classifier']
    model.load_state_dict(checkpoint['state_dict'])
    model.class_to_idx = checkpoint['class_to_idx']
    return model

def predict(image_path, model, topk=5):
    """Predict the class of an image."""
    model.eval()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    image = process_image(image_path).to(device)

    with torch.no_grad():
        log_ps = model(image)
        ps = torch.exp(log_ps)
        top_p, top_class = ps.topk(topk, dim=1)

    idx_to_class = {v: k for k, v in model.class_to_idx.items()}
    top_classes = [idx_to_class[i] for i in top_class.cpu().numpy()[0]]
    return top_p.cpu().numpy()[0], top_classes

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Predict the class of an image using a trained model")
    parser.add_argument('image_path', type=str, help="Path to the image")
    parser.add_argument('checkpoint', type=str, help="Path to the model checkpoint")
    parser.add_argument('--top_k', type=int, default=5, help="Number of top predictions to return")
    parser.add_argument('--category_names', type=str, help="Path to JSON file mapping categories to names")
    parser.add_argument('--gpu', action='store_true', help="Use GPU if available")
    args = parser.parse_args()

    # Load the model
    model = load_checkpoint(args.checkpoint)

    # Make predictions
    probs, classes = predict(args.image_path, model, args.top_k)

    # Map categories to names if a JSON file is provided
    if args.category_names:
        import json
        with open(args.category_names, 'r') as f:
            cat_to_name = json.load(f)
        classes = [cat_to_name[c] for c in classes]

    # Print results
    for prob, class_name in zip(probs, classes):
        print(f"{class_name}: {prob:.3f}")

if __name__ == "__main__":
    main()
