#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: LULUH ALYAHYA
# DATE CREATED: 18.11.2024                                  
# REVISED DATE: 
# PURPOSE: Create a function that retrieves the following 3 command line inputs 
#          from the user using the Argparse Python module. If the user fails to 
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
import argparse  # This module helps handle command-line arguments

def get_input_args():
    """
    Gets 3 command-line arguments from the user. If not provided, default values are used.
    
    Command-Line Arguments:
        1. --dir: Folder containing pet images (default is 'pet_images').
        2. --arch: CNN model architecture (default is 'vgg').
        3. --dogfile: File with dog names (default is 'dognames.txt').
    
    Returns:
        args: An object with the parsed command-line arguments.
    """

    # Step 1: Create the argument parser object
    # This object will handle the command-line arguments
    parser = argparse.ArgumentParser(
        description="This program classifies images using a CNN model and checks their results."
    )

    # Step 2: Add the command-line arguments
    # Argument 1: Path to the images directory
    parser.add_argument(
        '--dir',  # Name of the argument when called in the terminal
        type=str,  # The argument should be a string
        default='pet_images',  # Default folder name if the user doesn’t provide one
        help="Folder containing pet images. Default is 'pet_images'."  # Help text
    )

    # Argument 2: CNN model architecture to use
    parser.add_argument(
        '--arch',  # Name of the argument
        type=str,  # The argument should be a string
        default='vgg',  # Default is the VGG model
        help="CNN model architecture to use. Default is 'vgg'."  # Description of the argument
    )

    # Argument 3: File containing dog names
    parser.add_argument(
        '--dogfile',  # Name of the argument
        type=str,  # This argument is a string
        default='dognames.txt',  # Default file name
        help="File containing dog names. Default is 'dognames.txt'."  # Description for this argument
    )

    # Step 3: Parse the arguments
    # This will take the arguments from the command line and store them in an object
    args = parser.parse_args()

    # Debugging: Print the arguments to check if they are parsed correctly
    print("Parsed Arguments:")  # Debugging print
    print(f"  --dir: {args.dir}")  # Prints the directory path
    print(f"  --arch: {args.arch}")  # Prints the CNN model name
    print(f"  --dogfile: {args.dogfile}")  # Prints the dog file name

    # Return the parsed arguments object
    return args

# Debugging example: Uncomment to test directly in a script
# if __name__ == "__main__":
#     args = get_input_args()