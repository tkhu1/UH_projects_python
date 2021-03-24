#!/usr/bin/env python3

import sys
import traceback

# BEGIN SOLUTION
# please import only standard modules and make sure that your code compiles and runs without unhandled exceptions 
from Crypto.Cipher import AES
# END SOLUTION


def problem_1():
    with open("cipher1.bin", "rb") as cipher_file:
        cipher_text = cipher_file.read()

    # BEGIN SOLUTION
    key = bytes(list(range(1, 17)))          #generates key of bytes with values 1,2,3,...
    iv = bytes([0] * 16)                     #generates iv of bytes with values of all 0s
    cipher = AES.new(key, AES.MODE_CBC, iv)  #gets the AES cipher in CBC mode with no padding
    plain_text = cipher.decrypt(cipher_text) #calls decrypt function and returns plain text
    # END SOLUTION

    with open("plain1.txt", "wb") as plain_file:
        plain_file.write(plain_text)


def problem_2():
    with open("cipher2.bin", "rb") as cipher_file:
        cipher_text = cipher_file.read()
    
    # BEGIN SOLUTION
    modified_cipher_text = cipher_text[:]
    modified_cipher_text = cipher_text[32:48] + cipher_text[16:32] + cipher_text[0:16] 
    #tried 1,2,3 // 1,3,2 // 2,1,3 // 2,3,1 // 3,1,2 // 3,2,1 until the right order is found at 3,2,1
    
    #start decryption
    key = bytes(list(range(1, 17)))                   #generates key of bytes with values 1,2,3,...
    iv = bytes([0] * 16)                              #generates iv of bytes with values of all 0s
    cipher = AES.new(key, AES.MODE_CBC, iv)           #gets the AES cipher in CBC mode with no padding
    plain_text = cipher.decrypt(modified_cipher_text) #calls decrypt function and returns plain text
    #end decryption
    # END SOLUTION

    with open("plain2.txt", "wb") as plain_file:
        plain_file.write(plain_text)


def problem_3():
    with open("cipher3.bmp", "rb") as cipher_file:
        cipher_bmp = cipher_file.read()
    with open("msg3.bmp", "rb") as message_file:
        other_bmp = message_file.read()

    # BEGIN SOLUTION
    modified_cipher_bmp = cipher_bmp[:]
    #copies the first 2000 bytes from the msg3 bmp and the rest of the cipher bmp to a new bmp
    modified_cipher_bmp = other_bmp[0:2000] + cipher_bmp[2000:-1]
    # END SOLUTION

    with open("cipher3_modified.bmp", "wb") as modified_cipher_file:
        modified_cipher_file.write(modified_cipher_bmp)


def problem_4():
    with open("plain4A.txt", "rb") as plain_file:
        plain_text_a = plain_file.read()
    with open("cipher4A.bin", "rb") as cipher_file:
        cipher_text_a = cipher_file.read()
    with open("cipher4B.bin", "rb") as cipher_file:
        cipher_text_b = cipher_file.read()

    # BEGIN SOLUTION
    #many-time PAD vulnerability -> plain_text_a XOR cipher_text_a XOR cipher_text_b = plain_text_b    
    
    #bitwise XOR each byte in the above objects via 'for loops' to find plain_text_b  
    pA_XOR_cA = bytes(a ^ b for (a, b) in zip(plain_text_a, cipher_text_a))
    plain_text_b = bytes(a ^ b for (a, b) in zip(pA_XOR_cA, cipher_text_b)) 
    # END SOLUTION

    with open("plain4B.txt", "wb") as plain_file:
        plain_file.write(plain_text_b)


def problem_5():
    with open("cipher5.bin", "rb") as cipher_file:
        cipher_text = cipher_file.read()

    # BEGIN SOLUTION
    
    #initializes key containing the birthday of the Napoleon of Crime
    napoleon_birthday = list([0] * 16) 
    
    #three for loops to brute force the birthday in the key
    for month in range(1,13):
      for day in range(1,32):
        for year in range(1,100):
          napoleon_birthday[0] = month
          napoleon_birthday[1] = day
          napoleon_birthday[2] = year

          key = bytes(list(napoleon_birthday))         #generates key of bytes with values 1,2,3,...
          iv = bytes([0] * 16)                         #generates iv of bytes with values of all 0s
          cipher = AES.new(key, AES.MODE_CBC, iv)      #gets the AES cipher in CBC mode with no padding
          text_candidate = cipher.decrypt(cipher_text) #calls decrypt function and returns plain text
          
          #checks every byte in the decrypted candidate text to see if all bytes are valid English UTF-8
          isDecrypted = True
          for byte in text_candidate:
            if not byte <= 128:
              isDecrypted = False
          #if all valid, sets result text to candidate text
          if isDecrypted:
            plain_text = text_candidate
            
    '''
       Decrypted plain5.txt reads:
       "The location is St. Pancras railway station. Sincerely, Professor Moriarty"

       When you discover the location of the meeting, you immediately notify Inspector Lestrade. 
       He and Inspector Bradstreet assemble a team of detectives and rush to the railway station. 
       They arrive just in time to arrest both Moriarty's agent and Mr. Moran. Unfortunately, the 
       dastardly Professor Moriarty once again escapes. He is truly the Napoleon of crime. Nonetheless, 
       the detectives recover the Koh-i-Noor diamond and return it to the Tower of London. Dr. Watson 
       turns to you and says: "Excellent cryptanalysis!" to which you reply "Elementary, my dear Watson."
    '''
    # END SOLUTION

    with open("plain5.txt", "wb") as plain_file:
        plain_file.write(plain_text)


def main():
    try:
        problem_1()
        problem_2()
        problem_3()
        problem_4()
        problem_5()
    except Exception:
        print("Exception:")
        traceback.print_exc(file=sys.stdout)


if __name__ == "__main__":
    main()
