# Athenians        #
# CSC 442/CYEN 301 #
# XOR Crypto       #
# April 16, 2019   #
####################

#Github link: https://github.com/QueenShorty/CyberStorm/edit/WorkingInProgress/XOR%20Cyrpto/XOR.py

import sys
import fileinput
import binascii
        
def xor():
        #If you want to use open up a different key, make sure to change the file name (ex. "key" to "key2" or vice versa)
        with open("key", "r") as file: #reads the file, key
             hold = file.read() #Will hold the contents of key

        data = "" #Will hold the contents of the input file
        for line in fileinput.input():#read from stdin to grab ciphertext/plaintext
            data = data + line #Appends each line to the end of data

        message = map(bin, bytearray(data)) #Converts the contents of the input file to binary numbers
        key = map(bin, bytearray(hold)) #Converts the contents of the key to binary numbers

        answer = "" #Will hold the binary answer after using XOR
        for i, _ in enumerate(message): #loops through the message
            indexkey = i % len(key) #Used in case key is shorter than message
            xor = int(message[i], 2) ^ int(key[indexkey], 2) #Converts each binary number to int, then does XOR
            answer = answer + ("{0:08b}".format(xor)) #converts new number into binary in 8 number format

        break_up = [(answer[i*8:i*8+8]) for i in range(len(answer)/8)] #Breaks the input binary number into 8 so it can be converted to letters
        final = "" #Will hold the final solution
        for i in range(len(break_up)): #Loops through the lenth of break_up, which will be the same length as all the characters
            s = int(break_up[i], 2) #Converts the set of binary numbers into its base 10 numeric form
            final += chr(s) #Converts the numberic number (which is the same as the ASCII code) and converts it back to a character then adds it to the final answer
        print final
xor()

                                                                                

