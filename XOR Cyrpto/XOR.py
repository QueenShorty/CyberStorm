# Athenians        #
# CSC 442/CYEN 301 #
# XOR Crypto       #
# April 16, 2019   #
####################

#Github link: https://github.com/QueenShorty/CyberStorm/edit/WorkingInProgress/XOR%20Cyrpto/XOR.py

import sys
import fileinput
import binascii
#messagebit = []
keybit = []
bitxor = []
print "Hello World!"

#def strtobin(string): 
        #messagebit.append(bin(reduce(lambda x, y: 256*x+y, (ord(n) for n in string), 0)))
        #for i in string:
            #messagebit.append(bin(int(binascii.hexlify(i), 16)))

        
def xor():
        print "Hello World!"
        
        with open("key2", "r") as file:#reads the file, key
            x = file.read()
                #key = []#will hold the key
                #for line in file:
                        #key.append(line)

        for line in fileinput.input():#read from stdin to grab ciphertext/plaintext
            with open("ciphertext2", "r") as file:#reads plaintext
                data = file.read()
        message = map(bin, bytearray(data))
        #print message
        key = map(bin, bytearray(x))
        #print key
        print "for"
        a = len(message)
        b = len(key)

        if a == b:#if the key and message are the same length, xor them bit by bit
            answer = ""
            for i, _ in enumerate(message):
                xor = int(message[i], 2) ^ int(key[i], 2)
                answer = answer + ("{0:08b}".format(xor))

            #print answer

            break_up = [(answer[i*8:i*8+8]) for i in range(len(answer)//8)] #Breaks the input binary number into 7s or 8s with the range being the total number of binary numbers divided by 7 or 8
            final = "" #Will hold the final solution
            for i in range(len(break_up)): #Loops through the lenth of break_up, which will be the same length as all the characters
                s = int(break_up[i], 2) #Converts the set of binary numbers into its base 10 numeric form
                final += chr(s) #Converts the numberic number (which is the same as the ASCII code) and converts it back to a character then adds it to the final answer
            print(final) #prints the final decoded message
                

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

                                                                                

