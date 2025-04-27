import ast  # For safely reading the dictionary from the file
from PIL import Image  # To open and process images
import torchvision.transforms as transforms  # For image transformations like resizing and cropping
from torch.autograd import Variable  # For wrapping tensors in older PyTorch versions
import torchvision.models as models  # To load pretrained models
from torch import __version__  # To check the PyTorch version

# Load pretrained CNN models
# These models are already trained on ImageNet data
resnet18 = models.resnet18(pretrained=True)  # ResNet-18 model
alexnet = models.alexnet(pretrained=True)  # AlexNet model
vgg16 = models.vgg16(pretrained=True)  # VGG-16 model

# Create a dictionary to store models
# This makes it easy to select a model by its name
models = {'resnet': resnet18, 'alexnet': alexnet, 'vgg': vgg16}

# Load the class labels for ImageNet
# These are human-readable labels corresponding to model predictions
with open('imagenet1000_clsid_to_human.txt') as imagenet_classes_file:
    # Parse the file content into a dictionary
    # We use ast.literal_eval to make sure the parsing is safe
    imagenet_classes_dict = ast.literal_eval(imagenet_classes_file.read())

def classifier(img_path, model_name):
    """
    Classifies an image using a pretrained model.
    
    Parameters:
        img_path (str): The path to the image file.
        model_name (str): The name of the model to use ('resnet', 'alexnet', or 'vgg').

    Returns:
        str: The predicted class label for the image.
    """
    # Open the image using PIL
    img_pil = Image.open(img_path)  # This creates an image object

    # Preprocess the image to make it compatible with the CNN models
    # The transformations are based on what the models expect
    preprocess = transforms.Compose([
        transforms.Resize(256),  # Resize the image so the shortest side is 256 pixels
        transforms.CenterCrop(224),  # Crop the image to 224x224 pixels in the center
        transforms.ToTensor(),  # Convert the image to a PyTorch tensor (required for models)
        transforms.Normalize(  # Normalize using ImageNet's mean and standard deviation
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])
    
    # Apply preprocessing to the image
    img_tensor = preprocess(img_pil)  # Now the image is ready for the model

    # Add a batch dimension to the tensor
    # Models expect a batch of images, even if it's just one image
    img_tensor.unsqueeze_(0)  # Change shape from [C, H, W] to [1, C, H, W]

    # Check the PyTorch version to decide how to handle tensors
    pytorch_ver = __version__.split('.')  # Split version number into parts

    # If PyTorch version is 0.4 or higher, we don't need Variables
    if int(pytorch_ver[0]) > 0 or int(pytorch_ver[1]) >= 4:
        # Make sure the tensor doesn't require gradients
        # This is important for inference, where we don't update weights
        img_tensor.requires_grad_(False)

    # If PyTorch version is below 0.4, we must use Variable
    else:
        # Wrap the tensor in a Variable for compatibility with older PyTorch versions
        # We use volatile=True because this is for inference only
        data = Variable(img_tensor, volatile=True)

    # Get the selected model from the dictionary
    # This retrieves the model based on the name provided
    model = models[model_name]  # 'resnet', 'alexnet', or 'vgg'

    # Switch the model to evaluation mode
    # This disables things like dropout and batch norm updates
    model = model.eval()

    # Perform inference (get predictions)
    if int(pytorch_ver[0]) > 0 or int(pytorch_ver[1]) >= 4:
        # Use the tensor directly for PyTorch 0.4 and above
        output = model(img_tensor)
    else:
        # Use the Variable for older PyTorch versions
        output = model(data)

    # Find the index of the highest score in the output tensor
    # This corresponds to the predicted class
    pred_idx = output.data.numpy().argmax()

    # Return the class label corresponding to the predicted index
    return imagenet_classes_dict[pred_idx]
