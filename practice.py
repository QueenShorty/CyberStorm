import stat
import os
from ftplib import FTP
ftp = FTP('www.jeangourd.com')
ftp.login()
ftp.cwd('10')
x = []
x = ftp.nlst()
for f in x:
    print f
    
    #print '{0:010b}'.format(int(oct(stat.S_IMODE(os.lstat(f).st_mode)), 8))


