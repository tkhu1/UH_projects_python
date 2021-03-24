This program uses the Python Crypto.Cipher package to solve AES encryption and decryption problems. In each problem, the goal is to recover a plaintext (or at least some information about its contents). Each problem builds on the preceding one.


**Problem 1: The Game is Afoot**

You are at 221B Baker Street in the company of Dr. Watson, when the following e-mail arrives:


“Dear Mr. Sherlock Holmes,
I must once again ask you to help us as a consulting detective. Three days ago, the invaluable
Koh-i-Noor diamond was stolen from the Tower of London. We fear that the thieves are planning
to sell the diamond on the black market, where it may be lost forever. Fortunately, the thieves
acted hastily and they accidentally left a disk drive at the scene of the crime. We recovered two
files from this drive (please find them attached), but our detectives at Scotland Yard were not able
to make sense of them. We believe that the infamous Professor Moriarty is behind this spiteful
act, but our detectives have no leads to follow. Sherlock, you are our only hope!


Sincerely,
Inspector Lestrade”


The two files (cipher1.bin and msg1.txt) are used for this problem.


**Problem 2: The Jigsaw Puzzle**

You look at Dr. Watson... he has fallen asleep while you were busy decrypting the message. You
suspect that he would not be much help anyway, so you decide not to wake him up. Instead, you
look at the ciphertext and see that it is 48 bytes (384 bits) long, which means that it consists of
only three AES blocks, each being 16 bytes (128 bits) long. You can just try to rearrange the three
blocks in different ways (there are only 5 possibilities) to restore the ciphertext.


**Problem 3: Shaken, Not Stirred**

Dr. Watson wakes up, looks at the ciphertext, and scratches his head. Not a good sign, obviously.
It appears that you are on your own. You look at the ciphertext: it is a bitmap image (BMP file)
that has been encrypted using ECB block-cipher mode, so you should be able to see the patterns
of the plaintext. However, you cannot open the image since the header of the file is encrypted,
so no image-viewer program will be able to figure out how to display it (e.g., without the header,
a program will not know what the width and height of the image are). Suddenly, you get an idea:
what if the encrypted image has the same format as the plain one? You could restore the header
by copying the first few thousand bytes of the plain image (msg3.bmp) to overwrite the first
few thousand bytes of the third ciphertext (cipher3.bmp), and then open the modified
ciphertext in an image viewer!


**Problem 4: Same but Different**

It seems that your luck has run out: the cunning Professor Moriarty used a secure cipher, a secure
mode of operation, and a secure key. Dr. Watson is about to call Inspector Lestrade to tell him
that you cannot discover the location of the meeting, when you suddenly realize that Moriarty
made a mistake: he used the same key twice with CTR block-cipher mode, which is essentially a
stream cipher. Since you have one of the plaintexts (plain4A.txt) and both ciphertexts
(cipher4A.bin and cipher4B.bin) were XORed to the same pseudorandom sequence,
you should be able to easily recover the other plaintext!


**Problem 5: Checkmate**

Dr. Watson looks puzzled. How could he decrypt the ciphertext without knowing the mysterious
Professor Moriarty’s birthdate? To be fair, you do not have a clue about those three numbers
either. However, there are not that many possible combinations, so you could try to brute-force
the key. But how will you know which key is the correct one? Well, the plaintext is probably a
simple text file containing English text encoded in UTF-8 (or in ASCII). This means that the value
of every plaintext byte is between 0 and 128, which enables you to recognize a correctly
decrypted plaintext.