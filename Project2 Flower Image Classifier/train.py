import torch
from torch import nn, optim
from torchvision import datasets, transforms, models
from torchvision.models import VGG16_Weights
import os
import argparse

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Train a new network on a dataset")
    parser.add_argument('--data_dir', type=str, required=True, help="Directory containing training and validation data")
    parser.add_argument('--save_dir', type=str, default='.', help="Directory to save the checkpoint")
    parser.add_argument('--arch', type=str, default='vgg16', choices=['vgg16'], help="Model architecture")
    parser.add_argument('--learning_rate', type=float, default=0.001, help="Learning rate")
    parser.add_argument('--hidden_units', type=int, default=4096, help="Number of hidden units in the classifier")
    parser.add_argument('--epochs', type=int, default=5, help="Number of training epochs")
    parser.add_argument('--gpu', action='store_true', help="Use GPU if available")
    args = parser.parse_args()

    # Step 1: Data preprocessing
    # Define paths for training and validation datasets
    train_dir = os.path.join(args.data_dir, 'train')
    valid_dir = os.path.join(args.data_dir, 'valid')

    # Define data augmentation and normalization for the training set
    train_transforms = transforms.Compose([
        transforms.RandomResizedCrop(224),  # Randomly crop and resize images
        transforms.RandomRotation(30),  # Randomly rotate images
        transforms.RandomHorizontalFlip(),  # Randomly flip images horizontally
        transforms.ToTensor(),  # Convert images to PyTorch tensors
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])  # Normalize based on ImageNet stats
    ])

    # Define resizing and normalization for the validation set
    valid_transforms = transforms.Compose([
        transforms.Resize(256),  # Resize shorter side to 256 pixels
        transforms.CenterCrop(224),  # Center crop images to 224x224
        transforms.ToTensor(),  # Convert images to PyTorch tensors
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])  # Normalize based on ImageNet stats
    ])

    # Load datasets using ImageFolder
    train_data = datasets.ImageFolder(train_dir, transform=train_transforms)
    valid_data = datasets.ImageFolder(valid_dir, transform=valid_transforms)

    # Create DataLoaders for batch processing
    train_loader = torch.utils.data.DataLoader(train_data, batch_size=64, shuffle=True)
    valid_loader = torch.utils.data.DataLoader(valid_data, batch_size=64)

    # Step 2: Load a pre-trained model
    if args.arch == 'vgg16':
        weights = VGG16_Weights.DEFAULT
        model = models.vgg16(weights=weights)

    # Step 3: Freeze pre-trained parameters to prevent updates
    for param in model.features.parameters():
        param.requires_grad = False

    # Step 4: Define a new classifier
    input_features = model.classifier[0].in_features  # Number of input features for the classifier
    classifier = nn.Sequential(
        nn.Linear(input_features, args.hidden_units),  # Fully connected layer
        nn.ReLU(),  # Activation function
        nn.Dropout(0.2),  # Dropout for regularization
        nn.Linear(args.hidden_units, 102),  # Fully connected layer to output 102 classes
        nn.LogSoftmax(dim=1)  # Log-Softmax for output probabilities
    )
    model.classifier = classifier

    # Step 5: Define the loss function and optimizer
    criterion = nn.NLLLoss()  # Negative Log Likelihood Loss
    optimizer = optim.Adam(model.classifier.parameters(), lr=args.learning_rate)

    # Step 6: Set the device (GPU if available)
    device = torch.device("cuda" if args.gpu and torch.cuda.is_available() else "cpu")
    model.to(device)

    # Step 7: Training loop
    print("Starting training...")
    for epoch in range(args.epochs):
        model.train()  # Set model to training mode
        running_loss = 0

        for inputs, labels in train_loader:
            inputs, labels = inputs.to(device), labels.to(device)  # Move data to the device
            optimizer.zero_grad()  # Reset gradients
            log_ps = model(inputs)  # Forward pass
            loss = criterion(log_ps, labels)  # Compute loss
            loss.backward()  # Backward pass to compute gradients
            optimizer.step()  # Update weights
            running_loss += loss.item()

        # Validation loop
        model.eval()  # Set model to evaluation mode
        valid_loss = 0
        accuracy = 0

        with torch.no_grad():
            for inputs, labels in valid_loader:
                inputs, labels = inputs.to(device), labels.to(device)
                log_ps = model(inputs)
                valid_loss += criterion(log_ps, labels).item()
                ps = torch.exp(log_ps)
                top_p, top_class = ps.topk(1, dim=1)
                equals = top_class == labels.view(*top_class.shape)
                accuracy += torch.mean(equals.type(torch.FloatTensor)).item()

        print(f"Epoch {epoch + 1}/{args.epochs}.. "
              f"Train loss: {running_loss / len(train_loader):.3f}.. "
              f"Validation loss: {valid_loss / len(valid_loader):.3f}.. "
              f"Validation accuracy: {accuracy / len(valid_loader):.3f}")

    print("Training completed!")

    # Step 8: Save the checkpoint
    model.class_to_idx = train_data.class_to_idx
    checkpoint = {
        'architecture': args.arch,
        'classifier': model.classifier,
        'state_dict': model.state_dict(),
        'class_to_idx': model.class_to_idx,
        'optimizer_state': optimizer.state_dict(),
        'epochs': args.epochs
    }
    torch.save(checkpoint, os.path.join(args.save_dir, 'checkpoint.pth'))
    print("Model checkpoint saved!")

if __name__ == "__main__":
    main()
