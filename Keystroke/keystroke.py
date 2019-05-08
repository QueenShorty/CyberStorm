from pynput.keyboard import Key, Controller
from time import sleep 
from random import uniform
from termios import tcflush, TCIFLUSH
from sys import stdin, stdout

keyboard = Controller()

password = raw_input()
timings = raw_input()
print "password = {}".format(password)
print "timings = {}".format(timings)

password = password.split(",")
password = password[:len(password)/2 + 1]
password = "".join(password)

print password
timings = timings.split(",")
timings = [float(a) for a in timings]
keypress = timings[:len(timings)/2 + 1]
keyinterval = timings[len(timings)/2 + 1:]

print "key press times = {}".format(keypress)
print "key intevals = {}".format(keyinterval)

i = 0
for char in password:
    keyboard.press(char)
    sleep(uniform(keypress[i], keyinterval[i]))
    keyboard.release(char)

tcflush(stdout, TCIFLUSH)
print
