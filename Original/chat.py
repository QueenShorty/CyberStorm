# Athenians        #
# CSC 442/CYEN 301 #
# Chat Program     #
# April 24, 2019   #
####################

#Github link:https://github.com/QueenShorty/CyberStorm/blob/master/Chat%20Covert%20Channel/chat.py


import socket
from binascii import unhexlify
from time import time
import sys

#Time constants for covert message
ZERO = 0.025
ONE = 0.1

#Setup for the socket: IP and port can change
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "138.47.102.201"
port = 33333

#Connecting to the server
s.connect((ip, port))
#fill a data buffer with 4096 bytes
data = s.recv(4096)
#create an array to store the covert message
covert_bin = ""

#Recives the entire overt message
while (data.rstrip("\n") != "EOF"):
      sys.stdout.write(data)
      sys.stdout.flush()
      #calculate delay called delta
      t0 = time()
      data = s.recv(4096)
      t1 = time()
      delta = round(t1-t0, 3)
      #logic for unveiling the covert message
      if(delta >= ONE):
        covert_bin += "1"
      else:
        covert_bin += "0"
s.close()

covert = ""
i = 0
#Processes the covert binary string into ASCII
while (i < len(covert_bin)):
      #process one byte at a time
    b = covert_bin[i:i + 8]
      #convert it to ASCII
    n = int("0b{}".format(b), 2)
    try:
        covert += unhexlify("{0:x}".format(n))
    except TypeError:
        covert += "?"

      #stop at the string "EOF"
    i += 8

print(covert[0:-4])
