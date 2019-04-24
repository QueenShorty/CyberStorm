####################
# The Athenians    #
# CSC 442/CYEN 301 #
# Steg             #
# April 21, 2019   #
####################

#Github link: https://github.com/QueenShorty/CyberStorm/edit/WorkingInProgress/

#Example: python steg.py -(bB) -(sr) -o<val> -i[<val>] -w<val> [-h<val>]

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

#store from left to right : but for cyberstorm might be right to left

#with open(wrapper, "rb") as image:
  #f = image.read()
  #b = bytearray(f)
  #print b[1]

#f = open('/empty.jpg', 'wb')
#f.write(bytearray(b))
#f.close()

def format2():
    offset = sys.argv[3]
    interval = sys.argv[4]
    wrapper = sys.argv[5]

    if offset[:2] == "-o":
        print(offset[2:])
    else:
        print("Need -o followed by a number")
        
    if interval[:2] == "-i":
        print(interval[2:])
    else:
        print("Need -i followed by a number")

    if wrapper[:2] == "-w":
        print(wrapper[2:])
    else:
        print("Need -w followed by a file name")  

def format():
    data = sys.argv[2]

    if data == "-s":
        print("IN -s")
        hidden = sys.argv[6]
        format2()
        
        if hidden[:2] == "-h":
            print(hidden[2:])        

    elif data == "-r":
        print("IN -r")
        format2()

    else:
        print("Need -s or -r")


method = sys.argv[1]

if method == "-B":
    print("IN -B")
    format()

elif method == "-b":
    print("IN -b")
    format()

                     
