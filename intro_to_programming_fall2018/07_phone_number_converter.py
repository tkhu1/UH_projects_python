#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tyler Hu 
COSC 1306

1. Program identifies the words associated with telephone numbers by using dictionaries by reading in three and four letter words and 
   then have the user provide a number. 
2. Using that number, the program determines the words associated with the number by reading a list of words from a “words.txt” file 
   into a list, removing the new-line character at the end and filtering out the three and four-letter words.
"""

# digit to letter data
converter = {'0':['O'],
           '1':['I', 'L'],
           '2':['A', 'B', 'C'],
           '3':['D', 'E', 'F'],
           '4':['G', 'H', 'I'], 
           '5':['J', 'K', 'L'],
           '6':['M', 'N', 'O'], 
           '7':['P', 'Q', 'R', 'S'],
           '8':['T', 'U', 'V'], 
           '9':['W', 'X', 'Y', 'Z']}
    
# finds all possible letter combos according to input length
def get_combo(x, y):
    # init value
    result = []
    for i in x:
        for j in y:
            result.append(i+j)
    #print(result) # debug
    return result

# returns list of all possible letter combos for input
def get_word(num, converter):
    # init value
    result = [""]
    for i in num:
        result = get_combo(result,
                    list(converter[i]))
    #print(result) # debug
    return result

# main IO
def main():             
    # init value
    real_words = []
    # builds list from input items in dictionary file
    with open("words.txt") as file:
        for word in file.readlines():
            # removes newline 
            word = word.strip()
            # filters for three and four letter words only
            if len(word) == 3 or len(word) == 4:
                real_words.append(word)
            
    # init value for first run
    user_choice = "Y"
    
    while user_choice.upper() == 'Y':
        user_phone = input("Please enter a phone number: ")
        
        # turns user input into a string of only numbers
        user_string = ""
        for num in user_phone:
            if num.isdigit():
                user_string += num
        
        # checks for valid input of phone number
        try:
            if float(user_string).is_integer() and len(user_string) == 7:
                # isolates the first three digits of the phone number
                first3num = user_string[0:3]
                # calls function to find letter combos
                first3letters = get_word(first3num, converter)
                #print(first2letters) # debug
                
                # isolates the last four digits of the phone number
                last4num = user_string[3:7]
                # calls function to find letter combos
                last4letters = get_word(last4num, converter)
                #print(last2letters) # debug
                
                # output
                print("\n"+"Results include..."+"\n")
                       
                # init value
                result = ''
                # checks sequentially through combo list for real words
                for x in first3letters:
                    for y in last4letters:
                        if x in real_words and y in real_words:
                            result = ''
                            result += x + '-' + y
                            print(result)
                if result == '':
                    print("None found!")  
            # returns back to loop start
            else:
                print("\n"+"Invalid input! Please try again.")
                continue
        # returns back to loop start
        except ValueError:
            print("\n"+"Invalid input! Please try again.")
            continue
        
        # prompts user to input again
        user_choice = input("Try another (Y/N)? ")
        
        # exits program
        if user_choice.upper() == 'N':
            print("\n"+"Good Bye!")
            break
        
        # loop that checks for invalid input of choice
        while user_choice.upper() != 'Y':
            if user_choice.upper() == 'N':
                print("\n"+"Good Bye!")
                # exits program
                break
            print("\n"+"Invalid input! Please try again.")
            # prompts user to input again
            user_choice = input("Try another (Y/N)? ")

# call main
main()
