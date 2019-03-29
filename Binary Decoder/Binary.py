####################
# The Athenians    #
# CSC 442/CYEN 301 #
# Binary Decoder   #
# March 29, 2019   #
####################

#Github link: https://github.com/QueenShorty/CyberStorm/tree/master

import sys #Used to allow stdin and stdout

def decode(user_input): #Will decode input binary numbers into characters using 7 and 8 bit
    key = 1 #Key will increase when binary number is divisible by 7 and 8
    if ((len(user_input)-1) % 7 == 0) and ((len(user_input)-1) % 8 == 0): #Checks to see if binary number is divisible by both 7 and 8
        key = 2 #Increases key so that later it will print the output for both 7 and 8 bit
        n = 7 #Sets n to 7 to first print 7 bit solution
    elif (len(user_input)-1) % 8 == 0: #Checks if only divisible by 8 and then sets n to 8
        n = 8 #Use 8 since this is bit 8
    elif (len(user_input)-1) % 7 == 0: #Checks if only divisible by 7 and then sets n to 7
        n = 7 #Use 7 since this is bit 7
    else: #If neither 7 nor 8, then throw an error
        print("Error invalid input")
    for c in range(key): #Loops 1 time if only 7 or 8 bit, but loops 2 times if divisible by 7 and 8. Should print out both solutions
        break_up = [(user_input[i*n:i*n+n]) for i in range(len(user_input)//n)] #Breaks the input binary number into 7s or 8s with the range being the total number of binary numbers divided by 7 or 8
        answer = "" #Will hold the final solution
        for i in range(len(break_up)): #Loops through the lenth of break_up, which will be the same length as all the characters
            s = int(break_up[i], 2) #Converts the set of binary numbers into its base 10 numeric form
            answer += chr(s) #Converts the numberic number (which is the same as the ASCII code) and converts it back to a character then adds it to the final answer
        print(answer) #prints the final decoded message
        n+=1 #Increases n (this will only be used if the binary numbers are divisible by both 7 and 8, will covert using 7 bit, then convert using 8 bit)

for line in sys.stdin:
    user_input = line #Copies line from stdin and saves it

decode(user_input) #Runs the binary decoder
