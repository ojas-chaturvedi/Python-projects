#Both Caesar and Vigenere Ciphers
import os
os.system('cls')
choice = True
def choose_function():
    print('Would you like to encrpyt or decrypt?')
    print('E = Encrpyt')
    print('D = Decrypt')
    print('Q = Quit')
    choose = input('Choose: ')
    choose = choose.upper()
    return choose
def encrpyt_function():
    word = input("Enter a message: ")
    wordList = list(word)
    encryptWord = []
    def printencrypt():
        print('Your encrypted word is: ' + ''.join(encryptWord))
    shift = int(input("Enter a shift: "))
    for i in range(len(wordList)):
        letter = wordList[i]
        if letter.islower():
            cletter = chr((ord(letter) - ord("a") + shift) % 26 + ord("a"))
            encryptWord.append(cletter)
        elif letter.isupper():
            cletter = chr((ord(letter) - ord("A") + shift) % 26 + ord("A"))
            encryptWord.append(cletter)
        else:
            cletter = letter
            encryptWord.append(cletter)
    printencrypt()
def decrypt_caesar():
    word = input("Enter a encrypted word: ")
    wordList = list(word)
    shift = input("Enter a word in the message: ")
    decrypt = True
    while decrypt == True:
        for i in range(1,27):
            decryptWord = []
            shiftNumber = i
            for s in range(len(wordList)):
                letter = wordList[s]
                if letter.islower():
                    cletter = chr((ord(letter) - ord("a") - shiftNumber) % 26 + ord("a"))
                    decryptWord.append(cletter)
                elif letter.isupper():
                    cletter = chr((ord(letter) - ord("A") - shiftNumber) % 26 + ord("A"))
                    decryptWord.append(cletter)
                else:
                    cletter = letter
                    decryptWord.append(cletter)
            check = ''.join(decryptWord)
            if shift in check:
                print('Your decrypted message is: ' + ''.join(decryptWord))
                decrypt = False
while choice == True:
    name = input('What is your name: ')
    print('Hello ' + name + ', hope you are having a great day!!')
    cipher = input('Which cipher do you want to use??\n1 = Caesar\n2 = Vigenere\nQ = Quit\nChoice: ')
    if cipher == '1':
        code = True
        while code == True:
            var = choose_function()
            if var == 'E':
                encrpyt_function()
            elif var == 'D':
                decrypt_caesar()
            elif var == 'Q':
                code = False
            else:
                print('Oops! You must have typed something wrong!') 
    elif cipher == '2':
        code = True
        while code == True:
            var = choose_function()
            if var == 'E':
                first = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(26)))
                last = dict(zip(range(26), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
                letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                message = input('Enter message to be encrypted(no symbols): ')
                message = message.upper()
                key = input('Enter the key to be used(no symbols): ')
                key = key.upper().replace(' ','')
                lm = len(message)
                lk = len(key)
                symbols_spaces = [i for i in range(lm) if message[i] == ' ']
                message2 = message.replace(' ','')
                lm = len(message2)
                if lk > lm:
                    key = key[:lm]
                else:
                    for i in range(lk,lm):
                        key += key[i%lk]
                cipher = [last[(first[message2[i]] + first[key[i]])%26] for i in range(lm)]
                for i in symbols_spaces:
                    cipher.insert(i,' ')
                cipher = ''.join(cipher)
                print('Original message: ' + message)
                print('Encrypted message: ' + cipher)
            elif var == 'D':
                first = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(26)))
                last = dict(zip(range(26), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
                letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                message = input('Enter message to be decrypted(no symbols): ')
                message = message.upper()
                key = input('Enter the key to be used(no symbols): ')
                key = key.upper().replace(' ','')
                lm = len(message)
                lk = len(key)
                symbols_spaces = [i for i in range(lm) if message[i] == ' ']
                message2 = message.replace(' ','')
                lm = len(message2)
                if lk > lm:
                    key = key[:lm]
                else:
                    for i in range(lk,lm):
                        key += key[i%lk]
                plain = [last[(first[message2[i]] - first[key[i]])%26] for i in range(lm)]
                for i in symbols_spaces:
                    plain.insert(i,' ')
                plain = ''.join(plain)
                print('Encrypted message: ' + message)
                print('Decrypted message: ' + plain)
            elif var == 'Q':
                code = False
            else:
                print('Oops! You must have typed something wrong!') 
    elif cipher == 'Q':
        choice = False
    else:
        print('Oops! You must have typed something wrong!')
