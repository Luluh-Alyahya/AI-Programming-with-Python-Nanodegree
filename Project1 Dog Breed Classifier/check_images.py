#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py

# PROGRAMMER: LULUH ALYAHYA
# DATE CREATED: 18.11.2024
# REVISED DATE: [Date]
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true labels extracted from filenames, and
#          summarizes the performance of the model for image classification.
# Importing modules to be used later
from time import time, sleep  # To measure program runtime and for delays
from print_functions_for_lab_checks import *  # To debug and test functions
from get_input_args import get_input_args  # For getting input arguments
from get_pet_labels import get_pet_labels  # To get pet labels from filenames
from classify_images import classify_images  # To classify pet images
from adjust_results4_isadog import adjust_results4_isadog  # To check dog status
from calculates_results_stats import calculates_results_stats  # To calculate stats
from print_results import print_results  # To print final program output

def main():
    """
    This is the main function that runs the whole program. It has steps:
    1. Read arguments from the user (like directory and model type).
    2. Get labels for pet images.
    3. Use CNN model to classify the images.
    4. Check if the labels belong to a dog or not.
    5. Calculate how well the model performed (accuracy and percentages).
    6. Print the results in a nice format.
    """

    # Step 1: Start time tracking for the program
    start_time = time()  # Note the current time to calculate total runtime later

    # Step 2: Get input arguments from the user
    # User specifies the directory, CNN model, and dog file
    in_arg = get_input_args()

    # Debug: Check if the input arguments are correct (Extra Debugging)
    print("Arguments received from the user:", in_arg)  # Print arguments to debug
    check_command_line_arguments(in_arg)  # Another debugging tool

    # Step 3: Create results dictionary for pet labels
    results = get_pet_labels(in_arg.dir)  # Extract labels from filenames

    # Debug: Check if pet labels are correctly created
    print("Labels generated for images:")  # Debugging: Print pet labels
    for key, value in results.items():
        print(f"File: {key}, Label: {value}")  # Print each label for clarity
    check_creating_pet_image_labels(results)

    # Step 4: Classify the images using the selected CNN model
    classify_images(in_arg.dir, results, in_arg.arch)

    # Debug: Verify if classifications are added to results dictionary
    print("\nClassification results added to the dictionary.")  # Debug statement
    check_classifying_images(results)

    # Step 5: Adjust results for 'is-a-dog' checks
    adjust_results4_isadog(results, in_arg.dogfile)

    # Debug: Ensure dog status flags are properly added
    print("\nChecking 'is-a-dog' status adjustments in results.")  # Debug statement
    for key, value in results.items():
        print(f"File: {key}, Pet Label: {value[0]}, Classifier Label: {value[1]}, Is Pet Dog: {value[3]}, Is Classifier Dog: {value[4]}")  # Verbose debug print
    check_classifying_labels_as_dogs(results)

    # Step 6: Calculate statistics for classification performance
    results_stats = calculates_results_stats(results)

    # Debug: Check the stats dictionary for correctness
    print("\nStatistics calculated for the model:")  # Debugging output
    for stat, value in results_stats.items():
        print(f"{stat}: {value}")  # Print each statistic
    check_calculating_results(results, results_stats)

    # Step 7: Print the results of the classification
    print_results(results, results_stats, in_arg.arch, True, True)

    # Step 8: End time tracking and calculate total runtime
    end_time = time()  # Record end time
    tot_time = end_time - start_time  # Calculate total elapsed time in seconds

    # Print the runtime in hh:mm:ss format
    print("\n** Total Elapsed Runtime:",  # Print statement
          str(int((tot_time / 3600))) + ":" +  # Hours
          str(int((tot_time % 3600) / 60)) + ":" +  # Minutes
          str(int((tot_time % 3600) % 60)))  # Seconds


# Call the main function to start the program
if __name__ == "__main__":
    main()