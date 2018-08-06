import string, math
class cipher:
#Declare variables
    key,letterList,wordList,cipherDict,cipherDict2,fPath=15,[],[],{},{},"Keywords.txt"
    f,rawLetters = open(fPath, "r"),r"%s"%(string.printable)
    outString,decryptedString="",""
    message = """\nBeginning of message:\nabcdefghijklmnopqrstuvwxyz
1234567890-=\n+-`~
/\\/,.><[]{\t}\t\nEnd of message"""
#-------Populate lists and dictionaries------------
#list for letters
    def __init__(self):
        for letter in self.rawLetters:
            self.letterList.append(letter)

#list for words
        for line in self.f:
            self.wordList.append(line.replace("\n",""))
        self.f.close() #close file after read

#dictionary with both
        for i in range(0, len(self.letterList)):
            self.cipherDict[self.letterList[i]]=self.wordList[i]
#dictionary with both (reversed)
        for i in range(0, len(self.letterList)):
            self.cipherDict2[self.wordList[i]]=self.letterList[i]
#----------encode permutation----------------
    def shift(self,str1):
        temp,temp2,temp3=str1.encode("hex"),'',''
        #separate message into temp3 and temp2 (a, b)
        for i in range (0, len(temp)-1,2):
            temp2+=temp[i+1]
            temp3+=temp[i]
        temp=''
        #permute temp3 (a)
        for i in range(0,len(temp3)):
            temp+=temp3[(i+3)%(len(temp3))]
        temp3=temp
        temp=''
        #permute temp2(b)
        for i in range(0,len(temp2)):
            temp+=temp2[(i+3)%(len(temp2))]
        temp2=temp
        temp=''
        #combine temp3 and temp2 with temp3 in reverse order(-a+b)
        for i in range(0,len(temp3)):
            temp+=temp3[-1*i]+temp2[i]
        return temp
#----------decode permutation----------------
    def deshift(self,str1):
        temp,temp2,temp3='','',''
        #separate pairs with the first in reverse order (a, b)
        for i in range (0, len(str1)-1,2):
            temp2+=str1[i+1]
            temp3+=str1[-i]
        temp=''
        #permute temp2(b)
        for i in range(0,len(temp2)):
            temp+=temp2[(i-3)%(len(temp2))]
        temp2=temp
        temp=''
        #permute temp3 (a)
        for i in range(0,len(temp3)):
            temp+=temp3[(i-3)%(len(temp3))]
        temp3=temp
        temp=''
        #combine temp3 and temp2 with temp3 in order(a+b)
        for i in range(0,len(temp3)):
            temp+=temp3[i]+temp2[i]
        return temp.decode("hex")
#----------Encrypt message with cipher----------------
    def encrypt(self,str2,key):
        str1,offset,tempstring,tempstring2 = str2,key,"",""
        #permute original message by the first digit of the key
        for i in range(0,len(str1)):
            char = str1[i]
            for j in range(0,len(self.rawLetters)):
                if char==self.rawLetters[j]:
                    offset+=1
                    tempstring+=self.rawLetters[(j+int(math.floor(15*math.sin(offset))))%len(self.rawLetters)]
        offset=key+5
        for i in range(0,len(tempstring)):
            char = tempstring[i]
            for j in range(0,len(self.rawLetters)):
                if char==self.rawLetters[j]:
                    offset+=1
                    tempstring2+=self.rawLetters[(j+int(math.floor(15*math.cos(offset))))%len(self.rawLetters)]
        return tempstring2
#----------Decrypt message with cipher----------------
    def decrypt(self,str2, key):
        offset,tempstring,tempstring2 = key+5,"",""
        for i in range(0,len(str2)):
            char = str2[i]
            for j in range(0,len(self.rawLetters)):
                if char==self.rawLetters[j]:
                    offset+=1
                    tempstring+=self.rawLetters[(j-int(math.floor(15*math.cos(offset))))%len(self.rawLetters)]
        offset=key
        for i in range(0,len(tempstring)):
            char = tempstring[i]
            for j in range(0,len(self.rawLetters)):
                if char==self.rawLetters[j]:
                    offset+=1
                    tempstring2+=self.rawLetters[(j-int(math.floor(15*math.sin(offset))))%len(self.rawLetters)]
        return tempstring2
#----------Encrypt message----------------
    def encryptWords(self,msg):
        tempString = ""
        msg1 = self.encrypt(msg, self.key)
        for let in self.shift(msg1):
            tempString+=self.cipherDict[let]+" "
        return tempString
#----------Decrypt message----------------
    def decryptWords(self,msg):
        tempString = msg.split(" ")
        for i in range(0, len(tempString)-1):
            tempString[i]=tempString[i].replace(tempString[i], self.cipherDict2[str(tempString[i])])
            #print tempString
        encryptedString = "".join(tempString)
        return self.decrypt(self.deshift(encryptedString),self.key)
#----------For Testing Purposes----------------
    def xyTable(self):
        temp="1"
        for i in range(0,25):
            print "(%s,%s)\n"%(len(str(int(temp))), len(self.encryptWords(str(int(temp)))))
            temp+="1"
#Test the functions
cipher1 = cipher()
encrypted = cipher1.encryptWords(cipher1.message)
decrypted = cipher1.decryptWords(encrypted)
print "%s\n%s"%(encrypted,decrypted)
