#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: LULUH ALYAHYA
# DATE CREATED: 18.11.2024                
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
from os import listdir  # Importing listdir to access the files in a folder

def get_pet_labels(image_dir):
    """
    Creates a dictionary (`results_dic`) with pet labels extracted from image filenames.
    These labels are in lowercase and free from extra spaces.

    Parameters:
        image_dir (str): Path to the folder containing pet images.

    Returns:
        results_dic (dict): Dictionary with:
            - Key: Image filename (string)
            - Value: List with one item:
                     - Index 0: Pet label (string)
    """
    # Create an empty dictionary to store results
    results_dic = {}

    # Step 1: Get all filenames in the directory
    # listdir() gives a list of all file names in the specified folder
    filenames = listdir(image_dir)

    # Debugging: Print all filenames for verification
    print("Filenames in directory:", filenames)  # Optional debug print

    # Step 2: Loop through each filename to create labels
    for filename in filenames:
        # Ignore hidden files like .DS_Store (these start with '.')
        if filename[0] != ".":  # Check if the first character is not '.'
            # Debugging: Print each filename being processed
            print(f"Processing file: {filename}")

            # Step 3: Split the filename into parts by underscore
            # Example: "golden_retriever_123.jpg" -> ["golden", "retriever", "123.jpg"]
            parts = filename.lower().split("_")  # Convert to lowercase before splitting

            # Debugging: Print the parts of the filename
            print(f"Filename parts: {parts}")

            # Step 4: Filter out non-alphabetic parts (e.g., numbers, file extensions)
            # Join the remaining words with a space to create the label
            pet_label = " ".join([word for word in parts if word.isalpha()]).strip()

            # Debugging: Print the generated pet label
            print(f"Generated pet label: '{pet_label}'")

            # Step 5: Add the filename and label to the dictionary
            # Check if the filename is already in the dictionary
            if filename not in results_dic:
                results_dic[filename] = [pet_label]
            else:
                # Print a warning if a duplicate filename is encountered
                print(f"Warning: Duplicate filename '{filename}' detected!")

    # Debugging: Print the final dictionary before returning it
    print("Final results dictionary:", results_dic)

    # Return the dictionary with filenames and labels
    return results_dic