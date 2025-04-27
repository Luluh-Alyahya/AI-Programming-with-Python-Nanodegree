#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#
# PROGRAMMER: LULUH ALYAHYA
# DATE CREATED: 19.11.2024
# REVISED DATE: 
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). 

def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints the results of the classification, including summary statistics and
    optional details about misclassified dogs and breeds.
    
    Parameters:
      results_dic (dict): A dictionary containing information about images and their classification.
      results_stats_dic (dict): A dictionary with calculated statistics like counts and percentages.
      model (str): The CNN model architecture used for classification.
      print_incorrect_dogs (bool): Whether to print incorrectly classified dogs.
      print_incorrect_breed (bool): Whether to print incorrectly classified dog breeds.
    
    Returns:
      None: Prints directly to the console.
    """
    # Print the model architecture used
    print("\n\n*** Results Summary for CNN Model Architecture:", model.upper(), "***\n")
    
    # Print the number of images and their types
    print("Total Images: {:2d}".format(results_stats_dic['n_images']))
    print("Number of Dog Images: {:2d}".format(results_stats_dic['n_dogs_img']))
    print("Number of Non-Dog Images: {:2d}".format(results_stats_dic['n_notdogs_img']))
    
    # Print percentage statistics
    print("\n*** Statistics (Percentages) ***")
    for key, value in results_stats_dic.items():
        if key.startswith('pct'):  # Only print percentages
            print("{:20}: {:.1f}%".format(key, value))  # Format to 1 decimal place

    # Check and print incorrectly classified dogs
    if print_incorrect_dogs and (
        results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'] != results_stats_dic['n_images']):
        print("\n*** Incorrectly Classified Dog Images ***")
        incorrect_dogs_found = False
        for key, value in results_dic.items():
            if (value[3] == 1 and value[4] == 0) or (value[3] == 0 and value[4] == 1):
                incorrect_dogs_found = True
                print("Image: {:>30} | Pet Label: {:>20} | Classifier Label: {:>30}".format(
                    key, value[0], value[1]))
        if not incorrect_dogs_found:
            print("No incorrectly classified dog images found.")

    # Check and print incorrectly classified dog breeds
    if print_incorrect_breed and (
        results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']):
        print("\n*** Incorrectly Classified Dog Breeds ***")
        incorrect_breeds_found = False
        for key, value in results_dic.items():
            if value[3] == 1 and value[4] == 1 and value[2] == 0:
                incorrect_breeds_found = True
                print("Image: {:>30} | Pet Label: {:>20} | Classifier Label: {:>30}".format(
                    key, value[0], value[1]))
        if not incorrect_breeds_found:
            print("No incorrectly classified dog breeds found.")
