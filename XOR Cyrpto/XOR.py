####################
# The Athenians    #
# CSC 442/CYEN 301 #
# XOR Crypto       #
# April 16, 2019   #
####################

#Github link: https://github.com/QueenShorty/CyberStorm/edit/WorkingInProgress/XOR%20Cyrpto/XOR.py
import sys
import fileinput

def xor():
        m = []#holds plaintext/ciphertext

    with open("key", "r") as file:#reads the file, key
          k = []#will hold the key
          for line in file:
          k.append(line)

        for line in fileinput.input():#read from stdin to grab ciphertext/plaintext
          pass
        a = len(m)
        b = len(k)

        if a == b:#if the key and message are the same length, xor them bit by bit
          bitxor = m ^ k
          print bitxor
              
        elif a < b:#if the key is longer, cut off enough elements so it is the same length as the message
          bitxor = m ^ k[0:a]
          print bitxor

        #if the message is longer,keep looping through the key until you've gone through all of the message bits

        else:
