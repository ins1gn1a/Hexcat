#!/usr/bin/env python3

import sys
import os

with open(sys.argv[1],'r') as passfile:
    passlist = passfile.read().splitlines()

def decode_hex(password):
    decoded = []
    pwd = password
    if "$HEX" in password:
        #multihex = 
        multihex = list(filter(None, password.split("$")))

        for x in multihex:
            if "HEX[" in x:
                endhex = x.find("]")    
                decoded.append((bytes.fromhex(x[4:endhex]).decode("utf-8")))
            else:
                decoded.append(x)

        if len(decoded) != 0:
            pwd = ''.join(decoded)
        return (pwd)

    else:
        return (pwd)

for line in passlist:
    username,password = line.split(":",1)
    print (username + ":" + str(decode_hex(password)))
