import string
from random import choice as RDC

def Getpass(passlenght):
    password= string.ascii_letters + string.digits
    passlist=[]
    for passcode in range(passlenght):
        randpass = RDC(password)
        passlist.append(randpass)
    finpass="".join(passlist)
    return finpass
    
