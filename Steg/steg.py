####################
# The Athenians    #
# CSC 442/CYEN 301 #
# Steg             #
# April 21, 2019   #
####################

#Github link: https://github.com/QueenShorty/CyberStorm/edit/WorkingInProgress/

#Example: python steg.py -(bB) -(sr) -o<val> -w<val> [-h<val>]

#-b Use the bit method
#-B Use the byte method
#-s Store (and hide) data
#-r Retrieve hidden data
#-o<val> Set offset to <val>
#-i<val> Set interval to <val>
#-w<val> Set wrapper file to <val>
#-h<val> Set hidden file to <val>



from math import *
import sys
from PIL import Image


#method = sys.argv[1]
#data = sys.argv[2]
#offset = sys.argv[3]
#interval = sys.argv[4]
wrapper = sys.argv[1]
#hidden = sys.argv[6]

#store from left to right : but for cyberstorm might be right to left

with open(wrapper, "rb") as image:
  f = image.read()
  b = bytearray(f)
  #print b[1]

f = open('/empty.jpg', 'wb')
f.write(bytearray(b))
f.close()
                     
