#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tyler Hu 
COSC 1306

1. Program reads from a large corpus of text from a file and searches for a specific string (user inputted password). 
2. Program reads all the data into a list and then searches the list with both linear and binary searches to look for a string 
   provided by the user. Program does not use the keyword 'in' to search the list (restricted by Professor).
3. Program includes code to count the number of comparisons needed to execute the searches and outputs the count for both the linear 
   and binary search.
"""

# Does a linear search
def linear_search(password_list, password):
    # Init value for counter
    low = 0 
    # Search counter
    linear_count = 1
    while low < len(password_list):
        if password_list[low] == password:
            # Returns counter value if password is found
            return linear_count
        low += 1
        linear_count += 1
    # Returns false if password not found    
    return False

# Does a binary search
def binary_search(password_list, password):
    # Init value where the password could be
    low = 0 
    # Init value for the highest index where the password could be
    high = len(password_list) - 1 
    # Init value for max iterations (search counter)
    binary_count = 0
    # Loops through every item in passwords list
    while low <= high: 
        # Finds the middle index
        mid = (low + high)//2 
        # Corrects the max iteration number if user input matches position 0 in passwords list
        if password_list[mid] == password and password_list[0] == password:
            binary_count += 1
            # Returns tuple representing true if password is found
            return 1, binary_count+1
        # Returns tuple representing true if password is found 
        elif password_list[mid] == password:
            binary_count += 1
            return 1, binary_count
        # Splices out the passwords index from the middle to end if password is not found
        elif password_list[mid] > password:
            binary_count += 1
            high = mid - 1
        # Splices out the passwords index from the middle to beginning if password is not found
        else:
            binary_count += 1
            low = mid + 1    
    # Returns tuple representing false if password not found
    return 0, binary_count

# Main function I/O
def main():
    # Lets user know program is read writing from data
    print("Reading password data ...", end= ' ')
    
    # Stores strings from file
    passwords = []
    file = open('passwords_short.txt')
    for password in file.readlines():
        passwords.append(password.strip())
        # Sorts the list
        passwords.sort()
        file.close()
        # print(passwords) debug - to see the list
        
    # Lets user know program is done read writing
    print("Complete!")
    
    # Init value for user choice
    user_choice = 'Y'
    # Loops while user wants to try passwords
    while user_choice == 'Y':
        # User input
        user_password = input("Please enter the password to search for: ")
        
        # Searches via linear function for user password in the list
        print("\n"+"Linear Search:", end= ' ')
        if linear_search(passwords, user_password) != False:
            print("Password found after", linear_search(passwords, user_password), "tries")
        else:
            print("Password NOT found after", len(passwords), "tries")
    
        # Searches via binary function for user password in the list
        print("Binary Search:", end= ' ')
        # Contains returned tuple
        binary_result = binary_search(passwords, user_password)
        # Loops through tuple return
        if binary_result[0] == 0: 
            print("Password NOT found after", binary_result[1], "tries")
        else:
            print("Password found after", binary_result[1], "tries")
            print("\n"+"Password found! You should change your password!")
            
        # Gives user choice to continue or not
        user_choice = input("Do you want to search for another password? (Y/N): ").upper()
        # Prints exit message to user
        if user_choice != 'Y':
            print("\n"+"Goodbye!")

# Calls main function
main()
