# -*- coding: utf-8 -*-
"""
Tyler Hu 
COSC 1306

1. Program examines a set of words in a file to extract information about the frequency of letters. The file “zingarelli2005.txt” 
   contains a large number of words in Italian. Program provides a warning if this file does not exist. 
2. Program outputs the percent frequency for letters among all the words in the file, displayed to three decimal places (aligned).
3. Program calculates and outputs execution runtime.
4. This is important for certain decryption techniques, as it is useful to know how frequently letters occur in a given file.
"""

import string
import time

# main IO
def main ():
    # gets list of alphabet letters
    alpha = list(string.ascii_uppercase)
    # stores words from file
    words = ""
    # stores dictionary of key-letter (string) & value-number of appearances (int)
    result_dict = {}
    for letter in alpha:
        if letter not in result_dict:
            result_dict[letter] = 0
    
    # if read file exists
    try:
        with open("zingarelli2005.txt") as file:
            for word in file.readlines():
                #removes new-line character
                word = word.strip()
                words += word
                
        # loops through every letter in words and calculates number of appearances
        for letter in words:
            result_dict[letter] += 1
        
        # gets total number of letters from file            
        total_length = len(words)
        
        # output
        print("\n"+"The letter frequencies are:"+"\n")
        # loops and prints letter - frequency percentage rounded to three decimals
        for letter in alpha:
            print("{} - {:6.3f}%".format(letter, (result_dict[letter]/total_length)*100))
        
        #print(result_dict) #debug
        #print(total_length) #debug        
                
    # exits program if read file does not exist            
    except FileNotFoundError:
        print("\n"+"Error! File does not exist.")   
    
start = time.time()

# calls main function
main()

end = time.time()

# tests runtime
print("\n"+"Runtime - {} seconds.".format(end-start))        
