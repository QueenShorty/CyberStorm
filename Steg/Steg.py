####################
# The Athenians    #
# CSC 442/CYEN 301 #
# Steg             #
# April 24, 2019   #
####################

import sys

sentinel = [0000000, 1111111, 0000000, 0000000, 1111111, 0000000]

def retrievebit():
    o = get_offset()
    I = get_interval()
    w = wrapper_hidden()

def retrievebyte():
    o = get_offset()
    I = get_interval()
    w = wrapper_hidden()
    h = []

    i = 0
    while(i < len(w)):
        if(w[o] == "0000000"):
            temp = o
            j = 0
            while(j <= len(sentinel)):
                if(w[temp] == sentinel[j]):
                    temp += I
                    if(j == len(sentinel)):
                        return(h)
                    j += 1
                else:
                    j = len(sentinel) + 2

                
        else:
            h[i] = w[o]
            o += I
            i += 1
    

def storebyte():
    o = get_offset()
    I = get_interval()
    w = wrapper_hidden()
    h = wrapper_hidden()

    i = 0 
    while(i < len(h)):
        w[o] = h[i]
        o += I
        i += 1

    i = 0
    while(i < len(sentinel)):
        w[o] = sentinel[i]
        o += I
        i += 1
    
    return(w)

def storebit():
    o = get_offset()
    I = get_interval()
    w = wrapper_hidden()
    h = wrapper_hidden()

def get_offset():
    offset = 0
    for i in range(len(sys.argv)):
        test = sys.argv[i]
        if (test[:2] == "-o"):
            offset = test[2:]

    return(offset)

def get_interval():
    interval = 1
    for i in range(len(sys.argv)):
        test = sys.argv[i]
        if (test[:2] == "-i"):
            interval = test[2:]

    return(interval)

def wrapper_hidden():
    flag = False
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

def byte_maker(file_here):
    with open(file_here, "rb") as image:
        f = image.read()
        b = bytearray(f)
    return b
    
#Main

if((sys.argv[1] == "-b") and (sys.argv[2] == "-s")):
    storebit()
elif((sys.argv[1] == "-B") and (sys.argv[2] == "-s")):
    storebyte()
elif((sys.argv[1] == "-b") and (sys.argv[2] == "-r")):
    retrievebit()
elif((sys.argv[1] == "-B") and (sys.argv[2] == "-r")):
    retrievebyte()
else:
    print("Error")


