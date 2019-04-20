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
import sys

current = datetime.datetime.now() #Gets the current time
epoch = raw_input() #Gets the epoch time from stdin

def UTC(s): #Converts time from DST to UTC
    secs = time.mktime(s)
    r = time.gmtime(secs)
    return time.mktime(r) #Returns UTC in seconds for easier math

date = datetime.datetime.strptime(epoch, '%Y %m %d %H %M %S') #Formats from string to date
start = UTC(date.timetuple()) #Converts to tuple, then will return as seconds in UTC form
end = UTC(current.timetuple()) #Converts to tuple, then will return as seconds in UTC form

final = end - start #Subtracts both dates

if final % 60 != 0: #Checks to see if the number of seconds is divisible by 60
    final = final / 60 #Divides the number by 60
    final = int(final) #Gets rid of decimal places
    final = final * 60 #Multiplies this result by 60 to get a number within the 60 second interval
else:
    final = int(final) #Gets rid of decimal place if divisible by 60

md5 = hashlib.md5(str(hashlib.md5(str(final)).hexdigest())).hexdigest() #MD5 the number of seconds twice to get hash code

Alpha = "" #Will hold all the letters in hash
Num = "" #Will hold all the numbers in hash

for i in md5: #Goes through the hash code
    if i.isalpha() == True: #Checks if each character in hash is a letter
        Alpha += i #Adds letters to Alpha
    else:
        Num += i #Adds numbers to Num


Answer = Alpha[:2] + Num[-1] + Num[-2] #Combines the first two letters with the last two numbers

print(Answer)

