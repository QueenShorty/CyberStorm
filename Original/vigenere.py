####################
# The Athenians    #
# CSC 442/CYEN 301 #
# Vigenere Cipher  #
# March 29, 2019   #
####################

#Github link: https://github.com/QueenShorty/CyberStorm/tree/master

from math import *
import sys

Ciphertext =[]

def converter(Ki, Mi, n):
    #Here use an if to check -e or -d
    Code = sys.argv[1]
    if Code == "-e":
            C = (((Ki - n) + (Mi - n)) % 26) + n 

    elif Code == "-d":
            C = (((Mi - n) - (Ki - n)) % 26) + n
    else:
        print("Not a valid command, must use -e or -d")
                    
    C = chr(C)
    Ciphertext.append(C)            


def encoder():
    key = sys.argv[2]
    message = raw_input(" ")
    key = list(key)
    message = list(message)

    #enumerate method gets the index of message instead of the letter
    #this allows us to use the message index to control the key index
    for i, val in enumerate(message):
            m = message[i]

            while (ord(m) > 0 and ord(m) < 65) or (ord(m) > 90 and ord(m) < 97) or (ord(m) > 122):
                Ciphertext.append(m)
                #del message[i]
                if len(message)-1!= i:
                    print(len(message))
                    print(i)
                    del message[i]
                    m = message[i]
                else:
                    break
                    

            indexkey = i % len(key)
            #k is our letter based on index of key
            k = key[indexkey]
            if k == " ":
                del key[indexkey]
                k = key[indexkey]
                
            #checking for spaces to avoid the math
            if (ord(m) > 64 and ord(m) < 91): #Upper range
                #takes the letter value and gets the number val to do math
                temp = k.capitalize()
                print(temp)
                Ki = ord(temp)
                Mi = ord(m)
                n = 65
                converter(Ki, Mi, n)
                                
            elif (ord(m) > 96 and ord(m) < 122): #Lower range
                temp = k.lower()
                print(temp)
                Ki = ord(temp)
                Mi = ord(m)
                n = 97
                converter(Ki, Mi, n)
            
    print("Message: ")
    print("".join(message))
    print("Cipher: ")
    print("".join(Ciphertext))


encoder()



