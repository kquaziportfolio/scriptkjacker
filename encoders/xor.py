import random
import math
import string
def randomstr(dictionary=string.printable,leng=10):
    a=[]
    for i in range(leng):
        a.append(random.choice(dictionary))
    return a
def choose(p1,p2,p3,p4,c1,c2):
    if c1==c2==0:
        return p1
    elif c1==c2==1:
        return p4
    elif c1==0:
        return p2
    elif c1==1:
        return p3
    raise Exception("C1 and C2 must be 0 or 1")
def xorencode(message):
    if isinstance(message,str):
        message=message.encode()
    ptint=int.from_bytes(message,"little")
    ptbits=bin(ptint)
    ptbitstring=str(ptbits)[2:]
    ctbitstring="0b"
    maskbitstring="0b"
    for i in ptbitstring:
        r=random.randint(0,1)
        a,b=choose((1,1),(1,1),(0,1),(1,0),int(i),r)
        ctbitstring+=str(a)
        maskbitstring+=str(b)
    print(ctbitstring)
    ct=int.to_bytes(int(ctbitstring,2),len(ctbitstring)-2,"little")
    mask=int.to_bytes(int(maskbitstring,2),len(ctbitstring)-2,"little")
    return ct,mask
def xordecodepadded(ct,mask):
    ctint=int.from_bytes(ct,"little")
    maskint=int.from_bytes(mask,"little")
    ptint=ctint^maskint
    ptbitstring=str(bin(ptint))[2:]
    pt=int.to_bytes(ptint,len(ptbitstring),"little")
    return pt
def xordecode(ct,mask):
    pt=xordecodepadded(ct,mask)
    x=math.ceil((len(pt)+1)/8)
    pt=pt[:x]
    return pt
