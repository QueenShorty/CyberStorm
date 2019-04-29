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
        
        with open("key2", "r") as file:#reads the file, key
            x = file.read()

        for line in fileinput.input():#read from stdin to grab ciphertext/plaintext
            with open("ciphertext2", "r") as file:#reads plaintext
                data = file.read()

        message = map(bin, bytearray(data))
        key = map(bin, bytearray(x))

        answer = ""
        for i, _ in enumerate(message):
            xor = int(message[i], 2) ^ int(key[i], 2)
            answer = answer + ("{0:08b}".format(xor))
        print message[0]
        print key[0]
        print answer[0:8]

        break_up = [(answer[i*8:i*8+8]) for i in range(len(answer)/8)] #Breaks the input binary number into 7s or 8s with the range being the total number of binary numbers divided by 7 or 8
        final = "" #Will hold the final solution
        for i in range(len(break_up)): #Loops through the lenth of break_up, which will be the same length as all the characters
            s = int(break_up[i], 2) #Converts the set of binary numbers into its base 10 numeric form
            final += chr(s) #Converts the numberic number (which is the same as the ASCII code) and converts it back to a character then adds it to the final answer
        #print final #prints the final decoded message
        print message[1]
        print key[1]
        print answer[8:16]
        print final[1]

xor()

                                                                                

