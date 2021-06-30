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
        if currChar.isalpha() and (currChar in self.alphabetUC or currChar in self.alphabetLC):
            if currChar.islower():
                idx = self.alphabetLC.index(currChar)
                newChar = self.shiftedAlphabetLC[idx]
            else:
                idx = self.alphabetUC.index(currChar)
                newChar = self.shiftedAlphabetUC[idx]
        return newChar

#*************************************** End of Encryption Class **************************************************** 

class Summon:
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

    def validateKeys(self, allKeys):
        if "-" in allKeys:
            temp = allKeys.split("-")
            allKeys = "".join(temp)
        if allKeys.isdigit():
            if len(allKeys)!=24:
                return False
            for i in range(0, len(allKeys), 2):
                if int(allKeys[i:i+2])>26:
                    return False
            return True
        else:
            return False


#*************************************** End of Key Class ****************************************************


def clearSrc():
    os.system('clear' if os.name == 'posix' else 'cls')


def color(value):
    winToLin = {"0": "0", "1": "4", "2": "2", "3": "6", "4": "1", "5": "5", "6": "3", "7": "7", 
                "8": "0", "9": "4", "A": "2", "B": "6", "C": "1", "D": "5", "E": "3", "F": "7"}
    if os.name == "posix":
        os.system('tput setaf ' + winToLin[value])
    else:
        os.system('color ' + value)


def choseToEncrypt_manually():
    clearSrc()
    print('''--------------------------------------------------------------------
|                Encryption Services - Manual Mode                 |
--------------------------------------------------------------------
''')
    obj = Summon()
    obj.generateKey(12, 1, 26)
    userInput = input("Enter your message: ")
    print("\nYour key is:", obj.getKey(),"\n")
    print("Your encrypted message:\n")
    print(obj.encryptWithKeys(userInput))
    input("\n\nPress enter to continue...")


def choseToDecrypt_manually():
    clearSrc()
    print('''--------------------------------------------------------------------
|                Decryption Services - Manual Mode                 |
--------------------------------------------------------------------
''')
    userKeys = input("Enter your key: ")
    obj = Summon()
    isValid = obj.validateKeys(userKeys)
    if isValid == False:
        color('C')
        print("\nError: Invalid Keys\n\nPress any key to continue...")
        input()
        return
    obj.useKey(userKeys)
    msg = input("\nEnter you message: ")
    print("\nYour decrypted message:\n")
    print(obj.encryptWithKeys(msg))
    input("\n\nPress enter to continue...")

def chooseToEncrypt_file():
    clearSrc()
    print('''--------------------------------------------------------------------
|                Encryption Services - File Mode                   |
--------------------------------------------------------------------
''')
    print('''Select file... 
Selected file: ''', end='')
    Tk().withdraw()
    filename = askopenfilename()
    print(filename, '\n')

    text_file = open(filename, 'r')
    data = text_file.read()
    text_file.close()

    obj = Summon()
    obj.generateKey(12, 1, 26)
    print("\nYour key is:", obj.getKey(),"\n")
    data = obj.encryptWithKeys(data)

    text_file = open(filename, 'w')
    text_file.write(data)
    text_file.close()
    print('Your file has been encrypted.\n')
    input("\n\nPress enter to continue...")


def chooseToDecrypt_file():
    clearSrc()
    print('''--------------------------------------------------------------------
|                Decryption Services - File Mode                   |
--------------------------------------------------------------------
''')
    userKeys = input("Enter your key: ")
    obj = Summon()
    isValid = obj.validateKeys(userKeys)
    if isValid == False:
        color('C')
        print("\nError: Invalid Keys\n\nPress any key to continue...")
        input()
        return
    obj.useKey(userKeys)

    print('''\nSelect file... 
Selected file: ''', end='')
    Tk().withdraw()
    filename = askopenfilename()
    print(filename, '\n')

    text_file = open(filename, 'r')
    data = text_file.read()
    text_file.close()
    data = obj.encryptWithKeys(data)

    text_file = open(filename, 'w')
    text_file.write(data)
    text_file.close()
    print('Your file has been decrypted.\n')
    input("\n\nPress enter to continue...")


#******************************************** Main Program Starts ****************************************************

while True:
    clearSrc()
    color('E')
    print('''--------------------------------------------------------------------
|                             Welcome                              |
--------------------------------------------------------------------
''')
    choice1 = input('''Available Services:
    
    Press 1: To Encrypt
    Press 2: To Decrypt

    Press 0: To Exit
    
    Enter your choice here: ''').strip()

    if choice1 == '0':
        clearSrc()
        color('7')
        break

    elif choice1 == '1':
        while True:
            clearSrc()
            color('B')
            print('''--------------------------------------------------------------------
|                       Encryption Services                        |
--------------------------------------------------------------------
''')
            choice2 = input('''Supported Modes:
    
    Press 1: To enter message manually
    Press 2: To select a text file

    Press 0: To get back to the Main Menu
    
    Enter your choice here: ''').strip()

            if choice2 == '0':
                break
            elif choice2 == '1':
                choseToEncrypt_manually()
            elif choice2 == '2':
                chooseToEncrypt_file()
            else:
                print("\n    Error! Couldn't recoganize your choice. Try again.", end="")
                color('C')
                input()
    
    elif choice1 == '2':
        while True:
            clearSrc()
            color('A')
            print('''--------------------------------------------------------------------
|                       Decryption Services                        |
--------------------------------------------------------------------
''')
            choice2 = input('''Supported Modes:
    
    Press 1: To enter message manually
    Press 2: To select a text file

    Press 0: To get back to the Main Menu
    
    Enter your choice here: ''').strip()

            if choice2 == '0':
                break
            elif choice2 == '1':
                choseToDecrypt_manually()
            elif choice2 == '2':
                chooseToDecrypt_file()
            else:
                print("\n    Error! Couldn't recoganize your choice. Try again.", end="")
                color('C')
                input()

    else:
        print("\n    Error! Couldn't recoganize your choice. Try again.", end="")
        color('C')
        input()