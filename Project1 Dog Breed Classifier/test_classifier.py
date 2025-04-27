#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND/intropylab-classifying-images/test_classifier.py
#                                                                             
# PROGRAMMER: LULUH ALYAHYA                                                    
# DATE CREATED: 20.11.2024                                 
# REVISED DATE:             <=(Date Revised - if any)                         
# PURPOSE: To demonstrate the proper usage of the classifier() function that 
#          is defined in classifier.py This function uses CNN model 
#          architecture that has been pretrained on the ImageNet data to 
#          classify images. The only model architectures that this function 
#          will accept are: 'resnet', 'alexnet', and 'vgg'. See the example
#          usage below.
#
# Usage: python test_classifier.py    -- will run program from commandline

# Import the classifier function from the classifier.py script
from classifier import classifier

# Step 1: Define a test image
# The image should be in the 'pet_images' folder. Replace with a valid filename
# if "Collie_03797.jpg" doesn't exist in your folder.
test_image = "pet_images/Collie_03797.jpg"

# Debugging: Print the test image path to ensure it is correct
print("Test Image Path:", test_image)  # Optional debugging

# Step 2: Specify the CNN model architecture to use
# Supported models are: 'vgg', 'alexnet', and 'resnet'. it can be switch between these
# to test how different models classify the same image.
model = "vgg"  # Change this to 'resnet' or 'alexnet' for other models

# Debugging: Print the model name to ensure it is correctly set
print("Selected Model Architecture:", model)  # Debugging

# Step 3: Classify the image using the specified model
# The `classifier()` function takes the image path and model name as input and
# returns a string with the predicted label(s) for the image.
# Example output: "collie, sheepdog"
image_classification = classifier(test_image, model)

# Debugging: Print the raw classification output for inspection
print("Raw Classification Output:", image_classification)  # Debugging

# Step 4: Print the classification results
# This will display the image file name, the model used, and the classification result.
print("\n*** Results from test_classifier.py ***")
print("Image:", test_image)  # Print the test image name
print("Using Model:", model)  # Print the model architecture used
print("Classified as:", image_classification)  # Print the classification result

# Additional Information: it can be modify the test image or model architecture above
# to test different scenarios. Make sure the image exists in the correct directory.