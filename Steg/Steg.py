####################
# The Athenians    #
# CSC 442/CYEN 301 #
# Steg             #
# April 24, 2019   #
####################

#####################################
#how to use:
#python Steg.py -(Bb) -(sr) -i<val> -o<val> -w<file> -h<file> > outputfile

import sys

sentinel = [0, 255, 0, 0, 255, 0]

def retrievebit():
    #get input information
    o = get_offset()
    I = get_interval()
    w = wrapper_hidden()
    h = []

    #pull all the bits
    i = 0
    while(i < len(w)):
        temp = 0
        #pull a byte
        for k in range(8):
            w[o] &= 1
            temp |= (w[o] << (7 - k))
            o += I
        #check if it is the start of sentinel
        if(temp == sentinel[0]):
            j = 0
            offset = o
            while(j <= len(sentinel)):
                temp2 = 0
                #get next byte
                for l in range(8):
                    w[offset] &= 1
                    temp2 |= (w[offset] << (7 - l))
                    offset += I
                #check next sentinel item
                if(temp2 == sentinel[j+1]):
                    j += 1
                    #if here its done
                    if(j == len(sentinel)-1):
                        return(h)
                else:
                    j += len(sentinel) + 2
                
        h.append(temp)
        i += 1
        

def retrievebyte():
    #get input
    o = get_offset()
    I = get_interval()
    w = wrapper_hidden()
    h = []

    #go through the byte array finding correct bytes
    i = 0
    while(i < len(w)):
        #check if byte is first thing in sentinel
        if(w[o] == sentinel[0]):
            temp = o
            j = 0
            #find next bytes and check
            while(j <= len(sentinel)):
                if(w[temp] == sentinel[j]):
                    temp += I
                    j += 1
                    #full sentinel found and get out
                    if(j == len(sentinel)):
                        return(h)

                if(w[temp] != sentinel[j]):
                    j += len(sentinel) + 2

        #add byte to hidden file     
        h.append(w[o])
        o += I
        i += 1
    

def storebyte():
    #get inputs
    o = get_offset()
    I = get_interval()
    w = wrapper_hidden()
    h = wrapper_hidden()

    #store hidden file
    i = 0 
    while(i < len(h)):
        w[o] = h[i]
        o += I
        i += 1

    #store sentinel
    i = 0
    while(i < len(sentinel)):
        w[o] = sentinel[i]
        o += I
        i += 1
    
    return(w)

def storebit():
    #get input
    o = get_offset()
    I = get_interval()
    w = wrapper_hidden()
    h = wrapper_hidden()

    #combined hidden file with sentinel
    h += sentinel
    i = o
    j = 0
    while (j < len(h)):
        #gets byte and changes last bit
        for k in range(8):
            w[i] &= 254
            w[i] |= ((h[j] & 128) >> 7)
            h[j] <<= 1 
            i += I
        j += 1

    return(w)   

def get_offset():
    offset = 0
    #gets offset from input
    for i in range(len(sys.argv)):
        test = sys.argv[i]
        if (test[:2] == "-o"):
            offset = test[2:]

    return(int(offset))

def get_interval():
    interval = 1
    #gets interval from input
    for i in range(len(sys.argv)):
        test = sys.argv[i]
        if (test[:2] == "-i"):
            interval = test[2:]

    return(int(interval))

def wrapper_hidden():
    flag = False
    #finds the file name to look up
    for i in range(len(sys.argv)):
        test = sys.argv[i]
        if (test[:2] == ("-w" or "-h")):
            file_here = test[2:]
            byte_array = byte_maker(file_here)
            flag = True
    
    if (flag == False):
        print("Error: No wrapper found")
        exit()
    
    return(byte_array)

#turns file into byte array
def byte_maker(file_here):
    with open(file_here, "rb") as image:
        f = image.read()
        b = bytearray(f)
    return b

#turns byte array back into file
def decode(bytes):
    print("".join(map(chr, bytes)))

#####    
#Main
#####

#checks for what kind of action that was input into command line
if((sys.argv[1] == "-b") and (sys.argv[2] == "-s")):
    output = storebit()
    decode(output)
elif((sys.argv[1] == "-B") and (sys.argv[2] == "-s")):
    output = storebyte()
    decode(output)
elif((sys.argv[1] == "-b") and (sys.argv[2] == "-r")):
    output = retrievebit()
    decode(output)
elif((sys.argv[1] == "-B") and (sys.argv[2] == "-r")):
    output = retrievebyte()
    decode(output)
else:
    print("Error")


