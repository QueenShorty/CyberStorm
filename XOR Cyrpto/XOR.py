# Athenians        #
# CSC 442/CYEN 301 #
# XOR Crypto       #
# April 16, 2019   #
####################

#Github link: https://github.com/QueenShorty/CyberStorm/edit/WorkingInProgress/XOR%20Cyrpto/XOR.py

import sys
import fileinput
messagebit = []
keybit = []
bitxor = []
print "Hello World!"

def strtobin(string): 
        messagebit.append(bin(reduce(lambda x, y: 256*x+y, (ord(n) for n in string), 0)))
def xor():
        
        print "Hello World!"
        
        with open("key", "r") as file:#reads the file, key
                key = []#will hold the key
                for line in file:
                        key.append(line)

        for line in fileinput.input():#read from stdin to grab ciphertext/plaintext
                                with open("plaintext", "r") as file:#reads plaintext
                        message = []#holds plaintext
                        for line in file:

                                message.append(line)
        strtobin(message)
        print key
        print "for"
        a = len(message)
        b = len(key)

        if a == b:#if the key and message are the same length, xor them bit by bit
                print "if"
                for i in range(a):
                        bitxor[i] = message[i] ^ key[i]
                print bitxor

        elif a < b:
                print "elif"
                for i in range(a):
                        bitxor[i] = message[i] ^ key[i]
                print message
                for i, val in enumerate(key):
                        indexkey = i % b
                        k = key[indexkey]
                        if k == "x":
                                del key[indexkey]
                                k = key[indexkey]
                print key
                print bitxor

        #if the message is longer,keep looping through the key until you've gone through all of the message bits

        else:
                temp = []
                print "else"
                for i in range(b):
                        temp[i] = key[i%b]
                print temp
                while b < a:
                        b.append[temp]

                for i in range(a):
                        bitxor[i] = message[i] ^ key[i]
                print bitxor


xor()

                                                                                

