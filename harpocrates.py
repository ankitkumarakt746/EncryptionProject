import os
import random
from tkinter import Tk
from tkinter.filedialog import askopenfilename

class Encryption:
    key = 0
    alphabetUC = "" 
    alphabetLC = ""
    shiftedAlphabetUC = ""
    shiftedAlphabetLC = ""
    
    def __init__(self, key):
        self.alphabetUC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.alphabetLC = "abcdefghijklmnopqrstuvwxyz"
        self.shiftedAlphabetUC = self.alphabetUC[key:] + self.alphabetUC[:key]
        self.shiftedAlphabetLC = self.alphabetLC[key:] + self.alphabetLC[:key]

    def encrypt(self, currChar):
        newChar = ""
        if currChar.isalpha():
            if currChar.islower():
                idx = self.alphabetLC.index(currChar)
                newChar = self.shiftedAlphabetLC[idx]
            else:
                idx = self.alphabetUC.index(currChar)
                newChar = self.shiftedAlphabetUC[idx]
        return newChar

#*************************************** End of Encryption Class **************************************************** 

class Key:
    bunch = {}

    def generateKey(self, n, start, stop):  #stop = 26 as it'll run till 25 
        choices = list(range(start, stop))
        for i in range(1, n+1):
            curr = random.choice(choices)
            self.bunch['k'+str(i)] = curr
            choices.pop(choices.index(curr))

    def useKey(self, key):
        temp = key.split("-")
        allKeys = "".join(temp)
        j = 1
        for i in range(0, len(allKeys), 2):
            self.bunch['k'+str(j)] = 26 - int(allKeys[i:i+2])
            j += 1
        print(self.bunch)

    def listToString(self, s):
        result = ""
        for element in s:
            result += element
        return result

    def encryptWithKeys(self, dataInput):
        enObj = {int(i):Encryption(self.bunch[k]) for i, k in enumerate(self.bunch)}
        lettersList = list(dataInput)
        turn = 0
        i = 0
        while i<len(lettersList) and True:
            currChar = lettersList[i]
            if currChar.isalpha():
                lettersList.pop(i)
                lettersList.insert(i, enObj[turn].encrypt(currChar))
                if turn == 11:
                    turn = 0
                    continue
                turn += 1
            i += 1
        return self.listToString(lettersList)

    def getKey(self):
        keys = self.bunch
        result = ""
        for i, k in enumerate(keys):
            if int(keys[k]) < 10:
                result += "0" + str(keys[k])
            else:
                result += str(keys[k])
            if (i+1)%2 == 0 and i<11:
                result += "-"
        return result

#*************************************** End of Key Class ****************************************************



#******************************************** Main Program Starts ****************************************************

while True:
    os.system('cls')
    os.system('color E')
    print('''--------------------------------------------------------------------
|                             Welcome                              |
--------------------------------------------------------------------
''')
    choice1 = int(input('''Available Services:
    
    Press 1: To Encrypt
    Press 2: To Decrypt

    Press 0: To Exit
    
    Enter your choice here: '''))

    if choice1 == 0:
        os.system('cls')
        break

    elif choice1 == 1:
        while True:
            os.system('cls')
            os.system('color B')
            print('''--------------------------------------------------------------------
|                       Encryption Services                        |
--------------------------------------------------------------------
''')
            choice2 = int(input('''Supported Modes:
    
    Press 1: To enter message manually
    Press 2: To select a text file

    Press 0: To get back to the Main Menu
    
    Enter your choice here: '''))
            if choice2 == 0:
                break
            elif choice2 == 1:
                choseToEncrypt_manually()
            elif choice2 == 2:
                chooseToEncrypt_file()
            else:
                print("Error! Couldn't recoganize your choice. Try again.")
    
    elif choice1 == 2:
        while True:
            os.system('cls')
            os.system('color A')
            print('''--------------------------------------------------------------------
|                       Decryption Services                        |
--------------------------------------------------------------------
''')
            choice2 = int(input('''Supported Modes:
    
    Press 1: To enter message manually
    Press 2: To select a text file

    Press 0: To get back to the Main Menu
    
    Enter your choice here: '''))
            if choice2 == 0:
                break
            elif choice2 == 1:
                choseToDecrypt_manually()
            elif choice2 == 2:
                chooseToDecrypt_file()
            else:
                print("Error! Couldn't recoganize your choice. Try again.")

    else:
        print("Error! Couldn't recoganize your choice. Try again.")
