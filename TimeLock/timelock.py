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
x = '2013 05 06 06 43 25 UTC' #Had to change the hour from 07 to 06 to get correct result. Not sure how to make it go back an hour if in Daylight Savings Time
y = '1999 12 31 23 59 59 UTC' #Didnt have to change this one since it is on normal time

def dates(s): #Takes string date and converts it to an integer date
    return datetime.datetime.strptime(s, '%Y %m %d %H %M %S %Z') #Just formatting stuff

start = dates(y) #Saves the earliest date here
end = dates(x) #Saves the most recent date here

delta = end - start #Subtracts both dates
print(delta.total_seconds()) #Prints out the subtracted dates in seconds
