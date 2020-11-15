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

    def encrypt(self, msg):
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
    for char in input:
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


def choseToEncrypt_manually():
    os.system('cls')
    print('''--------------------------------------------------------------------
|                Encryption Services - Manual Mode                 |
--------------------------------------------------------------------
''')
    while True:
        key1 = keyGenerate(1, 25)
        key2 = keyGenerate(1, 25)
        key3 = keyGenerate(1, 25)
        if key1 != key2 and key1 != key3 and key2 != key3:
            break 
    combinedkey = combineKeys(key1, key2, key3)
    userInput = input("Enter your message: ")
    print("\nYour key is:", combinedkey,"\n")
    print("Your encrypted message:\n")
    print(encrypt3Keys(userInput, key1, key2, key3))
    input("\n\nPress enter to continue...")


def splitKey(key):
    key1 = 26 - (int(key[:2]))
    key2 = 26 - (int(key[2:4]))
    key3 = 26 - (int(key[4:]))
    return key1, key2, key3


def choseToDecrypt_manually():
    os.system('cls')
    print('''--------------------------------------------------------------------
|                Decryption Services - Manual Mode                 |
--------------------------------------------------------------------
''')
    threeKeys = input("Enter your key: ")
    key1, key2, key3 = splitKey(threeKeys)
    if (key1>26 or key1<0) or (key2>26 or key2<0) or (key3>26 or key3<0):
        print("Invalid Key")
        return 
    else:
        msg = input("\nEnter you message: ")
        print("\nYour decrypted message:\n")
        print(encrypt3Keys(msg, key1, key2, key3))

    input("\n\nPress enter to continue...")


def chooseToDecrypt_file():
    os.system('cls')
    print('''--------------------------------------------------------------------
|                Decryption Services - File Mode                   |
--------------------------------------------------------------------
''')

    threeKeys = input("Enter your key: ")
    key1, key2, key3 = splitKey(threeKeys)
    if (key1>26 or key1<0) or (key2>26 or key2<0) or (key3>26 or key3<0):
        print("Invalid Key")
        return
    else:
        print('''\nSelect file... 
Selected file: ''', end='')
    Tk().withdraw()
    filename = askopenfilename()
    print(filename, '\n')

    text_file = open(filename, 'r')
    data = text_file.read()
    text_file.close()

    data = encrypt3Keys(data, key1, key2, key3)
    
    text_file = open(filename, 'w')
    text_file.write(data)
    text_file.close()

    print('Your file has been decrypted.\n')
    input("\n\nPress enter to continue...")


def chooseToEncrypt_file():
    os.system('cls')
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
    
    while True:
        key1 = keyGenerate(1, 25)
        key2 = keyGenerate(1, 25)
        key3 = keyGenerate(1, 25)
        if key1 != key2 and key1 != key3 and key2 != key3:
            break
    
    combinedkey = combineKeys(key1, key2, key3)
    print("Your key is:", combinedkey,"\n")
    data = encrypt3Keys(data, key1, key2, key3)
    
    text_file = open(filename, 'w')
    text_file.write(data)
    text_file.close()
    print('Your file has been encrypted.\n')
    input("\n\nPress enter to continue...")


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
