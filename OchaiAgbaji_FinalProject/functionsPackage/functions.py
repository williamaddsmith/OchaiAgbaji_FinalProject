# Name: Will Smith, Jared Skinner
# email: smith2w6@mail.uc.edu
# Assignment Title: Final Project
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: This project demonstrates that I can use Eclipse to decrypt data inside a json file and call my work using one function
# Citations: Spec from nicomp
# Anything else that's relevant:N/A
#functions.py

import json
from PIL import Image


def decrypt_Location_And_Show_Picture():
    # Open the JSON file
    with open('EncryptedGroupHints Spring 2023 Section 002.json', 'r') as f:
        # Load the JSON data into a Python dictionary
        data = json.load(f)
        # Access the encrypted location data for 'Ochai Agbaji'
        encrypted_location = data['Ochai Agbaji']
    # Close the JSON file
    f.close()

    # Open the English.txt file in read mode
    with open('English.txt', 'r') as f:
        # Read the lines of the file into a list
        lines = f.readlines()
    # Close the English.txt file
    f.close()

    # Decrypt the location data
    decrypted_location = ''
    for index in encrypted_location:
        # Subtract 1 from the index to account for 0-indexing
        decrypted_location += lines[int(index)-1].strip() + ' '
    # Remove the trailing space from the decrypted location
    decrypted_location = decrypted_location.rstrip()

    # Print the encrypted and decrypted location data for debugging
    print('Encrypted location:', encrypted_location)
    print('Decrypted location:', decrypted_location)
    
    # importing Image class from PIL package
     
    # creating a object
    im = Image.open(r"results.jpg")
 
    im.show()
                