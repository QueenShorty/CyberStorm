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

def interval(): #Format that includes interval (do not need to include math for finding interval)
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


def nointerval(): #Format that excludes interval when it is not present (do need to include math for finding interval)
    offset = sys.argv[3]
    wrapper = sys.argv[4]

    if offset[:2] == "-o":
        print(offset[2:])
    else:
        print("Need -o followed by a number")

    if wrapper[:2] == "-w":
        print(wrapper[2:])
    else:
        print("Need -w followed by a file name")


def format2(check, length): #This format checks if interval is included or not
    if check == 0 and length == 7: #For -s with -i
        hidden = sys.argv[6]
        interval()
        if hidden[:2] == "-h":
            print(hidden[2:])
    
    if check == 0 and length == 6: #For -s without -i
        hidden = sys.argv[5]
        nointerval()
        if hidden[:2] == "-h":
            print(hidden[2:])

    if check == 1 and length == 6: #For -r with -i
        interval()

    if check == 1 and length == 5: #For -r without -i
        nointerval()

            
def format(): #This format checks if -s or -r
    data = sys.argv[2]

    if data == "-s":
        print("IN -s")
        format2(0, len(sys.argv)) #Passes 0 to indicate -s and the length of arguments       

    elif data == "-r":
        print("IN -r")
        format2(1, len(sys.argv)) #Passes 1 to indicate -r and the length of arguments

    else:
        print("Need -s or -r")

###################################################################################
#This is where main begins
method = sys.argv[1]

if method == "-B": #For Byte method
    print("IN -B")
    format()

elif method == "-b": #For bit method
    print("IN -b")
    format()

else:
    print("Need -B or -b")
####################################################################################
                     
