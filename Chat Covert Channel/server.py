import socket
from binascii import hexlify

ZERO = 0.025
ONE=1

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 1337
    s.bind(("", port))
    s.listen(0)
except:
    print "Connection Error"


c, addr = s.accept()


msg = "Some message..."
covert = "secret" + "EOF"
covert_bin = ""

for i in covert:
    #convert each character to a full byte
    #hexlify converts ASCII to hex
    #int converts the hex to a decimal integer
    #bin provides its binary representation with a 0b prefix
    #    that needs to be removed
    #That's the [2:] (return the string from the third char on
    #zfill left-pads the bit string with 0s to ensure a full byte
    covert_bin += bin(int(hexlify(i), 16)) [2:].zfill(8)


n = 0
for i in msg:
    c.send(i)
    if(covert_bin[n] == 0):
        time.sleep(ZERO)
    else:
        time.sleep(ONE)
    n = (n+1) % len(covert_bin)
c.send("EOF")
c.close()
