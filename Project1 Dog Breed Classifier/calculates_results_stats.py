#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER: LULUH ALYAHYA
# DATE CREATED: 17.11.2024                               
# REVISED DATE: 
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the programrun using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the 
#          how to calculate the counts and percentages for this function.    
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value.  This dictionary should contain the 
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##
# TODO 5: Define calculates_results_stats function below, please be certain to replace None
#       in the return statement with the results_stats_dic dictionary that you create 
#       with this function
# 
def calculates_results_stats(results_dic):
    """
    Calculates statistics based on the results of the program run using the 
    classifier's model. Creates a dictionary with counts and percentages.
    """
    # Create variables to store counts
    n_images = len(results_dic)  # Total number of images
    n_dogs_img = 0  # Count of dog images
    n_notdogs_img = 0  # Count of non-dog images
    n_match = 0  # Count of correct matches
    n_correct_dogs = 0  # Count of correctly identified dog images
    n_correct_notdogs = 0  # Count of correctly identified non-dog images
    n_correct_breed = 0  # Count of correct dog breeds

    # Loop through the dictionary
    for key, value in results_dic.items():
        # Check if the pet label matches the classifier label
        if value[2] == 1:  # 1 means it's a match
            n_match += 1
        
        # Check if the image is a dog and classified correctly
        if value[3] == 1 and value[4] == 1:  # Both pet and classifier agree it's a dog
            n_correct_dogs += 1
        
        # Check if the image is NOT a dog and classified correctly
        if value[3] == 0 and value[4] == 0:  # Both pet and classifier agree it's not a dog
            n_correct_notdogs += 1
        
        # Check if the breed of the dog is correct
        if value[3] == 1 and value[2] == 1:  # It's a dog and labels match
            n_correct_breed += 1
        
        # Count the total number of dog images
        if value[3] == 1:  # 1 means it's a dog image
            n_dogs_img += 1

    # Calculate the number of non-dog images
    n_notdogs_img = n_images - n_dogs_img  # Total images minus dog images

    # Create a dictionary to store the statistics
    results_stats_dic = {}

    # Store the counts in the dictionary
    results_stats_dic['n_images'] = n_images  # Total images
    results_stats_dic['n_dogs_img'] = n_dogs_img  # Total dog images
    results_stats_dic['n_notdogs_img'] = n_notdogs_img  # Total non-dog images
    results_stats_dic['n_match'] = n_match  # Total correct matches
    results_stats_dic['n_correct_dogs'] = n_correct_dogs  # Total correct dog classifications
    results_stats_dic['n_correct_notdogs'] = n_correct_notdogs  # Total correct non-dog classifications
    results_stats_dic['n_correct_breed'] = n_correct_breed  # Total correct dog breed classifications

    # Store the percentages in the dictionary
    # Percentage of matches
    if n_images > 0:  # Avoid dividing by zero
        results_stats_dic['pct_match'] = (n_match / n_images) * 100.0
    else:
        results_stats_dic['pct_match'] = 0.0  # Set percentage to zero if no images

    # Percentage of correctly classified dogs
    if n_dogs_img > 0:  # Avoid dividing by zero
        results_stats_dic['pct_correct_dogs'] = (n_correct_dogs / n_dogs_img) * 100.0
    else:
        results_stats_dic['pct_correct_dogs'] = 0.0  # No dogs, so percentage is zero

    # Percentage of correctly classified dog breeds
    if n_dogs_img > 0:  # Avoid dividing by zero
        results_stats_dic['pct_correct_breed'] = (n_correct_breed / n_dogs_img) * 100.0
    else:
        results_stats_dic['pct_correct_breed'] = 0.0  # No dogs, so percentage is zero

    # Percentage of correctly classified non-dogs
    if n_notdogs_img > 0:  # Avoid dividing by zero
        results_stats_dic['pct_correct_notdogs'] = (n_correct_notdogs / n_notdogs_img) * 100.0
    else:
        results_stats_dic['pct_correct_notdogs'] = 0.0  # No non-dogs, so percentage is zero

    # Return the results statistics dictionary
    return results_stats_dic
