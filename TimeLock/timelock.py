####################
# The Athenians    #
# CSC 442/CYEN 301 #
# TimeLock         #
# April 16, 2019   #
####################

#Github link: https://github.com/QueenShorty/CyberStorm/edit/WorkingInProgress/TimeLock/timelock.py
import time
import datetime
import hashlib

#Example dates he gave on PDF
x = '2013 05 06 06 43 25' #Had to change the hour from 07 to 06 to get correct result. Not sure how to make it go back an hour if in Daylight Savings Time
y = '1999 12 31 23 59 59' #Didnt have to change this one since it is on normal time

def dates(s): #Takes string date and converts it to an integer date
    return datetime.datetime.strptime(s, '%Y %m %d %H %M %S') #Just formatting stuff

start = dates(y) #Saves the earliest date here
end = dates(x) #Saves the most recent date here

delta = end - start #Subtracts both dates
x = delta.total_seconds() #Stores the total number of seconds in x

print(x) #JUST FOR TESTING

#We probably need to optimize this
if x % 60 != 0: #Checks to see if the number of seconds is divisible by 60
    x = x / 60 #Divides the number by 60
    x = int(x) #Gets rid of decimal places
    x = x * 60 #Multiplies this result by 60 to get a number within the 60 second interval

print(x) #JUST FOR TESTING

test = hashlib.md5(str(hashlib.md5(str(x)).hexdigest())).hexdigest() #MD5 the number of seconds twice to get hash code

print(test) #JUST FOR TESTING

Alpha = "" #Will hold all the letters in hash
Num = "" #Will hold all the numbers in hash

for i in test: #Goes through the hash code
    if i.isalpha() == True: #Checks if each character in hash is a letter
        Alpha += i #Adds letters to Alpha
    else:
        Num += i #Adds numbers to Num


Answer = Alpha[:2] + Num[-1] + Num[-2] #Combines the first two letters with the last two numbers

print(Answer)
