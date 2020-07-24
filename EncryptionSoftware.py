"""
Bugs:

    > Bug 13.1 :

        Status      :   Fixed (on 22-07-2020)

        Goal        :   To ensure that all the three keys are different.

        Description :   There is some possibility that two or all three keys can be same. This 
                        will weaken the encryption.

"""



import random

class Encryption:
    alphabetUC = "" 
    alphabetLC = ""
    shiftedAlphabetUC = ""
    shiftedAlphabetLC = ""
    
    def __init__(self, key):
        self.alphabetUC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.alphabetLC = "abcdefghijklmnopqrstuvwxyz"
        self.shiftedAlphabetUC = self.alphabetUC[key:] + self.alphabetUC[:key]
        self.shiftedAlphabetLC = self.alphabetLC[key:] + self.alphabetLC[:key]

    def encrypt(self, msg):
        '''msg = []
        for ch in message:
            msg.append(ch)'''
        for i in range(0, len(msg), 1):
            currChar = msg[i]
            if currChar.isalpha():
                if currChar.islower():
                    idx = self.alphabetLC.index(currChar)
                    newChar = self.shiftedAlphabetLC[idx]
                    msg.pop(i)
                    msg.insert(i, newChar)
                else:
                    idx = self.alphabetUC.index(currChar)
                    newChar = self.shiftedAlphabetUC[idx]
                    msg.pop(i)
                    msg.insert(i, newChar)

        str1 =""
        for element in msg:
            str1 += element

        return str1 


#*************************************** End of Class **************************************************** 


def listToString(s):
    str = ""
    for element in s:
        str += element
    return str


def encrypt3Keys(input, key1, key2, key3):
    enObj1 = Encryption(key1)
    enObj2 = Encryption(key2)
    enObj3 = Encryption(key3)
    encrypted = []
    for char in input:                 #convert to list
        encrypted.append(char)
    turn = 1
    for i in range(0,len(encrypted),1):
        currChar = []
        currChar.append(encrypted[i])
        encrypted.pop(i)
        if turn == 1:
            encrypted.insert(i, enObj1.encrypt(currChar))
            turn+=1
        elif turn == 2:
            encrypted.insert(i, enObj2.encrypt(currChar))
            turn+=1
        else:
            encrypted.insert(i, enObj3.encrypt(currChar))
            turn=1
    return listToString(encrypted)

    
def keyGenerate(start, stop):
    key = random.randint(start, stop+1)
    return int(key)


def combineKeys(key1, key2, key3):
    k1 = str(key1)
    k2 = str(key2)
    k3 = str(key3)
    if key1<10:
        k1 = "0" + k1
    if key2<10:
        k2 = "0" + k2
    if key3<10:
        k3 = "0" + k3
    return k1+k2+k3


def choseToEncrypt():
    key1 = keyGenerate(1, 25)                                  #Bug 13.1    Status: Fixed
    key2 = keyGenerate(1, 25)                                  #Bug 13.1    Status: Fixed
    key3 = keyGenerate(1, 25)                                  #Bug 13.1    Status: Fixed
    while True:
        if key1 != key2 and key1 != key3 and key2 != key3:
            break  
    combinedkey = combineKeys(key1, key2, key3)
    userInput = input("Enter your message: ")
    print("Your key is :", combinedkey,"\n")
    print("Your encrypted message:\n", encrypt3Keys(userInput, key1, key2, key3))


def splitKey(key):
    key1 = 26 - (int(key[:2]))
    key2 = 26 - (int(key[2:4]))
    key3 = 26 - (int(key[4:]))
    return key1, key2, key3


def choseToDecrypt():
    threeKeys = input("Enter your key: ")
    key1, key2, key3 = splitKey(threeKeys)
    if key1>26 or key2>26 or key3>26:
        print("Invalid Key")
        return 
    else:
        msg = input("Enter you message: ")
        print("Your decrypted message:\n", encrypt3Keys(msg, key1, key2, key3))


#******************************************** Main Program Starts ****************************************************

repeat = 1
while repeat==1:
    choice1 = input("Press 1 to encrypt or 0 to decrypt: ")
    if choice1=='1':
        choseToEncrypt()
    elif choice1=='0':
        choseToDecrypt()
    else:
        print("Invalid Choice")
    choice2 = input("Press 'y' to continue or any other key to quit: ")
    if not(choice2=='y' or choice2=='Y'):
        repeat=0
