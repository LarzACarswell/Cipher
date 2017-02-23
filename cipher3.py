import string
import math
alp=r"{0}".format(string.printable)

def encrypt(str1, key):
    offset = key
    tempstring = ""
    tempstring2 = ""
    for i in range(0,len(str1)):
        char = str1[i].lower()
        for j in range(0,len(alp)):
            if char==alp[j]:
                offset+=1
                tempstring+=alp[(j+int(math.floor(15*math.sin(offset))))%len(alp)]
    offset=key+5
    for i in range(0,len(tempstring)):
        char = tempstring[i]
        for j in range(0,len(alp)):
            if char==alp[j]:
                offset+=1
                tempstring2+=alp[(j+int(math.floor(15*math.cos(offset))))%len(alp)]
    return tempstring2
def decrypt(str2, key):
    offset = key+5
    tempstring = ""
    tempstring2=""
    for i in range(0,len(str2)):
        char = str2[i]
        for j in range(0,len(alp)):
            if char==alp[j]:
                offset+=1
                tempstring+=alp[(j-int(math.floor(15*math.cos(offset))))%len(alp)]
    offset=key
    for i in range(0,len(tempstring)):
        char = tempstring[i]
        for j in range(0,len(alp)):
            if char==alp[j]:
                offset+=1
                tempstring2+=alp[(j-int(math.floor(15*math.sin(offset))))%len(alp)]
    return tempstring2

