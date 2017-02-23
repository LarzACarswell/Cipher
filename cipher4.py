import string
import re
import cipher3

letterList=[]
wordList=[]
cipherDict={}
cipherDict2={}
fPath = ".\\Keywords.txt"
f = open(fPath, "r")
rawLetters = r"{0}".format(string.printable)
outString=""
decryptedString = ""
message = """\nBeginning of message:\nabcdefghijklmnopqrstuvwxyz
1234567890-=\n+-`~
/\\/,.><[]{\t}\t\nEnd of message"""

#list for letters
for letter in rawLetters:
    letterList.append(letter)

#list for words
for line in f:
    wordList.append(line.replace("\n",""))
f.close() #close file after read

#dictionary with both
for i in range(0, len(letterList)):
    cipherDict[letterList[i]]=wordList[i]
#dictionary with both (reversed)
for i in range(0, len(letterList)):
    cipherDict2[wordList[i]]=letterList[i]


#----------Encrypt message----------------
def encryptWords(msg):
    tempString = ""
    msg1 = cipher3.encrypt(msg, 10)
    for let in msg1:
        tempString+=cipherDict[let]+" "
    return tempString

#----------Decrypt message----------------
def decryptWords(msg):
    tempString = msg.split(" ")
    #print tempString
    #tempString1=msg
    for i in range(0, len(tempString)-1):
        tempString[i]=tempString[i].replace(tempString[i], cipherDict2[str(tempString[i])])
        #print tempString
    encryptedString = "".join(tempString)
    
    return cipher3.decrypt(encryptedString,10)

#Test the functions
outString = encryptWords(message)
decryptedString = decryptWords(outString)
print "{0}\n\n{1}".format(message,decryptedString)
