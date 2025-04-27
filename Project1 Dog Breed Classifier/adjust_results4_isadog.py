#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: LULUH ALYAHYA
# DATE CREATED:  17.11.2024                               
# REVISED DATE: 
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results 
#          dictionary to indicate whether or not the pet image label is of-a-dog, 
#          and to indicate whether or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file. We recommend reading all the
#          dog names in dognames.txt into a dictionary where the 'key' is the 
#          dog name (from dognames.txt) and the 'value' is one. If a label is 
#          found to exist within this dictionary of dog names then the label 
#          is of-a-dog, otherwise the label isn't of a dog. Alternatively one 
#          could also read all the dog names into a list and then if the label
#          is found to exist within this list - the label is of-a-dog, otherwise
#          the label isn't of a dog. 
#         This function inputs:
#            -The results dictionary as results_dic within adjust_results4_isadog 
#             function and results for the function call within main.
#            -The text file with dog names as dogfile within adjust_results4_isadog
#             function and in_arg.dogfile for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           whether or not the pet image label is of-a-dog as the item at index
#           3 of the list and whether or not the classifier label is of-a-dog as
#           the item at index 4 of the list. Note we recommend setting the values
#           at indices 3 & 4 to 1 when the label is of-a-dog and to 0 when the 
#           label isn't a dog.
#
##
# TODO 4: Define adjust_results4_isadog function below, specifically replace the None
#       below by the function definition of the adjust_results4_isadog function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 

def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjust the dictionary to check if the labels are dogs or not.
    """
    # Create a set to store dog names
    dognames = set()
    
    # Open the file with dog names and read each line
    with open(dogfile, 'r') as f:
        for line in f:
            dogname = line.strip().lower()  # Remove spaces and make lowercase
            dognames.add(dogname)  # Add the name to the set
    
    # Counter for counting iterations
    counter = 0  
    
    # Loop through each item in the dictionary
    for key, value in results_dic.items():
        # Increment the counter
        counter += 1  
        
        # Check if the pet label is a dog
        if value[0] in dognames:
            is_pet_dog = 1  # It is a dog
        else:
            is_pet_dog = 0  # It is not a dog

        # Split classifier label into a list
        classifier_labels = [label.strip() for label in value[1].split(',')]

        # Variable to check classifier
        found_dog_in_classifier = False  
        for label in classifier_labels:
            if label in dognames:
                found_dog_in_classifier = True

        # Check if the classifier says it's a dog
        if found_dog_in_classifier:
            is_classifier_dog = 1  # Classifier says dog
        else:
            is_classifier_dog = 0  # Classifier says not a dog

        # Add the results to the dictionary
        value.extend([is_pet_dog, is_classifier_dog])

        # Condition based on the counter
        if counter % 5 == 0:
            pass  # Placeholder for future code
