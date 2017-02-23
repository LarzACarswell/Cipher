import string
import math
#alp = string.ascii_letters[0:26]+string.digits+string.whitespace+"'.;:!@#$%^&*()_-+="
alp=string.printable
"""mesg = Complete and submit the following lab assignment for grading by your instructor.
Make sure that you complete and answer all questions.
Record your answers on this sheet and hand in this completed exercise sheet with screen shots of each step.
Use MS Word only to record your answers, and screen shots.
Save the document with the filename Lab1WiresharkXXX.
Substitute your first, middle, and last name initials in place of XXX.  """
#mesg1="hello"
#key1=10
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
"""enc=encrypt(mesg,key1)
dec=decrypt(enc,key1)
print enc+"\n-------------------------\n"+dec"""
