#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: LULUH ALYAHYA
# DATE CREATED: 18.11.2024                               
# REVISED DATE: 
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Import the classifier function to classify images using a CNN model
from classifier import classifier  # This is the custom function for classification

def classify_images(images_dir, results_dic, model):
    """
    Classifies images using a pretrained CNN model and compares predictions 
    with the actual pet labels. Updates the results dictionary.

    Parameters:
      images_dir (str): Path to the folder containing the images to classify.
      results_dic (dict): Dictionary with:
                          - Key: Filename of the image (string)
                          - Value: A list containing:
                              - [0]: Actual label (pet image label) (string)
                              - [1]: (To be added) Classifier label (string)
                              - [2]: (To be added) Match flag (1 for match, 0 otherwise)
      model (str): CNN model architecture to use ('resnet', 'alexnet', 'vgg').

    Returns:
      None: Updates the `results_dic` dictionary in place.
    """

    # Loop through each image in the dictionary
    for image_filename, value in results_dic.items():
        # Step 1: Construct the full path to the image
        # Combine the directory with the filename to get the full path
        image_path = f"{images_dir}/{image_filename}"

        # Debugging: Print the full image path (just to check)
        print(f"Image path: {image_path}")  # Optional, helps ensure paths are correct

        # Step 2: Call the classifier function to classify the image
        # This returns a string with the predicted labels (e.g., 'Maltese dog, Maltese').
        classifier_label = classifier(image_path, model)

        # Debugging: Print the classifier label (for manual checking)
        print(f"Classifier output: {classifier_label}")  # Debug statement

        # Step 3: Format the classifier label
        # Convert to lowercase and remove spaces to ensure consistency in comparisons
        classifier_label = classifier_label.lower().strip()

        # Debugging: Check if formatting is correct
        print(f"Formatted Classifier Label: {classifier_label}")  # Debug statement

        # Step 4: Compare the pet label with the classifier label
        # Check if the actual pet label exists in the classifier's predicted labels
        pet_label = value[0]  # The actual label is the first item in the list
        match = 1 if pet_label in classifier_label else 0

        # Debugging: Print the comparison results
        print(f"Pet Label: {pet_label}, Match: {'Yes' if match else 'No'}")  # Debug output

        # Step 5: Update the results dictionary
        # Add the classifier label and match flag to the list in the dictionary
        value.extend([classifier_label, match])

        # Debugging: Print the updated dictionary entry
        print(f"Updated Entry for {image_filename}: {value}\n")  # Shows full updated entry