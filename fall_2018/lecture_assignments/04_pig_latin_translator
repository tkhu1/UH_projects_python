# -*- coding: utf-8 -*-
"""
Tyler Hu 
COSC 1306

1. Program asks the user for a word in English.
2. Program uses a function to translate that word into “Pig Latin” and returns the translated word.
3. Translation rules for “Pig Latin”:
   “Pig Latin” is a fictitious language derived from English using a few simple rules.
   a.) If a word starts with a vowel (a, A, e, E, i, I, o, O, u, U) then the translation is formed by adding a "way" to the end of 
       the word. e.g. "at" becomes "atway", "egg" becomes "eggway"
   b.) If a word contains no vowels (a, A, e, E, i, I, o, O, u, U) then the translation is formed by a adding a "way" to the end of 
       the word. e.g. "my" becomes "myway", "by" becomes "byway"
   c.) If a word starts with a consonant and contains a vowel, the translation is formed by moving the consonant(s) up to the first 
       vowel to the end of the word and adding an "ay". e.g. "bat" becomes "atbay", "that" becomes "atthay", "three" becomes "eethray"
   d.) Words that start with an initial capital letter should be translated to words with an initial capital letter. e.g. "Houston" 
       becomed "Oustonhay", "Iceland" becomes "Icelandway", "Marry" becomes "Arrymay"
"""

# checks if first letter is a vowel
def first_check(letter): 
    return letter.upper() in "AEIOU"

# checks for other vowels in word
def vowel_check(word):
    # checks every character in the word
    for letter in word:           
        # check if a character is a vowel
        if first_check(letter):   
            return True
    # if not vowel    
    return False                  
    
# chooses which output to display  
def translate(word): 
    # checks for first rule (starts with vowel)
    if vowel_check(word[0]) == True: 
        return word + "way"
    # results in second rule (no vowel)
    elif vowel_check(word) == False:
        return word + "way" 
    # results in third rule (starts with consonant)
    else:
        for letter in word:          
            if first_check(letter): 
                vowel_value = word.index(letter)
                # stops checking after first vowel
                break 
        # if first letter of the input word is capitalized         
        while word[0].isupper():     
            # splicer
            word = word[vowel_value:] + word[:vowel_value] 
            word = word[0].upper() + word[1:len(word)].lower() + "ay"
            return word
        # else if input word is all lowercase
        else:
            # splicer
            word = word[vowel_value:] + word[:vowel_value] + "ay" 
            return word

# debugging    
#word = three
#translate(word)    

# output
print("\n"+"This program will translate a word from English to Pig Latin.")        

# init value    
choice = "Y" 
    
# prints output    
while choice.upper() == "Y": 
    word = input("Please enter a word: ")
    print("\n" + word, "becomes", translate(word) + ".")
    choice = input("Would you like another word? (Y/N) ")
    
# program ends
else: 
    print("\n" + "Ankthay ouyay!") 
