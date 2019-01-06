# -*- coding: utf-8 -*-
"""
Tyler Hu 
COSC 1306

1. Program asks the user to input a code word and then use that word to encrypt a given message using the Vigenère cypher. The Vigenère 
   cypher uses a code word to scramble a plain-text message into an encrypted message. Generally, only alphabet characters are 
   encrypted, and non-letters are normally removed.
2. Program copies punctuation and spaces from the plain-text to the cypher-text - only the letters will be encrypted. Upper-case letters
   are encrypted to upper-case and lower-case to lower-case. To perform the encryption on some text, each letter in the text is matched 
   with a letter in the secret code. The letter in the secret code determine the offset applied to corresponding letter in the 
   plain-text. Each code letter produces an offset, for example “A” represents an offset of 0, “B” an offset of 1, “C” an offset of 2 
   and so on. A letter in plain-text, say “m” is encrypted by a code letter of “A” to “m”, by “B” to “n”, by “C” to “o” and so on. The 
   encryption that offsets a letter past “z” wraps back around to start with “a”.
"""
import string

# This is the plain-text to be encrypted. Do Not delete this!
plain_text = """A test string, just for practice - here in Houston."""

# This is the easy secret message for optional decryption
easy_secret = """S xgjx llvkek, cmwv wsk hvctxbui - jvvx ar Jfyllsp."""

# single letter encryptor
def encrypt_letter(text_letter, code_letter):
    alphabet = string.ascii_uppercase
    index = alphabet.find(code_letter)
    cypher = alphabet[index:]+alphabet[:index]
    cypher_index = alphabet.find(text_letter.upper())
    result = cypher[cypher_index]
    if text_letter.islower():
        result = result.lower()
    return result

# sentence encryptor
def encryptor(text, code):
    # iterates for all chars in input text
    mover = 0          
    # iterates for only ascii chars in input text
    cypher_mover = 0   
    # init strings
    output_text = ""
    cypher_text = ""
    for letter in text:
        # for upper case letters in input text
        if letter.isalpha() and letter.isupper():
            cypher_text = code[cypher_mover%len(code)]
            #print(cypher_text) # debug
            encrypted_text = encrypt_letter(text[mover], cypher_text)
            #print(encrypted_text) # debug
            output_text += encrypted_text.upper()
            mover += 1
            cypher_mover += 1
        # for lower case oetters in input text
        elif letter.isalpha() and letter.islower():
            cypher_text = code[cypher_mover%len(code)]
            #print(cypher_text) # debug
            encrypted_text = encrypt_letter(text[mover], cypher_text)
            #print(encrypted_text) # debug
            output_text += encrypted_text.lower()
            mover += 1
            cypher_mover += 1
        else:
            output_text += letter
            mover += 1
    return output_text

# asks the user for a code word and store it for use later
code_word = input("Enter the code word: ").upper()

# calls an encryption function with the plain text above and the code word and 
# saves the result it gives back (cypher-text)
final_text = encryptor(plain_text, code_word)

# print out the cypher-text <-- This is the goal of the assignment  
print("\n" + final_text)
