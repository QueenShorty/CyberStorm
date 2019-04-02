import stat
import os
from ftplib import FTP
ftp = FTP('www.jeangourd.com')
ftp.login()
ftp.cwd('7') #Goes to the 7 file
x = [] #Array that holds all the files and file permissions
w2 = "" #Holds the FINAL binary numbers to be tested in decoder
ftp.dir(x.append) #Appends the files and file permissions to x
for i in x: #Goes through each line
    s = i #Sets a string to each the line
    w = "" #Will hold 10 binary numbers
    for j in s[0:10]: #Loops through only file permission
        if j == "-": #if there is a -, then put a 0
            w = w + "0"
        else:
            w = w + "1" #if there is anything else, then put a 1
    for k in w[0:3]: #Checks if the first three binary numbers are a 1 (cuts out the noise)
        if k == "1": #If there is noise then reset w to an empty string
            w = ""
    w = w[3:10]
    
    w2 = w2 + w #Now append the 10 binary numbers to the final string
print w2
    #print '{0:010b}'.format(int(oct(stat.S_IMODE(os.lstat(f).st_mode)), 8))

def decode(user_input):
    n = 7
    #while ((len(user_input)-1) % 10 != 0):
        #user_input = user_input + "0"

    answer= ""
    break_up = [(user_input[i*n:i*n+n]) for i in range(len(user_input)//n)]

    for i in range(len(break_up)):
        s = int(break_up[i], 2)
        answer += chr(s)

    print(answer)

decode(w2)


