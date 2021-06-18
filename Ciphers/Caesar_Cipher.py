code = True
while code == True:
    print('Would you like to encrypt or decrypt?')
    print('E = Encrypt')
    print('D = Decrypt')
    print('Q = Quit')
    choose = input('Choose: ')
    choose = choose.upper()
    if choose == 'E':
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
    elif choose == 'D':
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
    elif choose == 'Q':
        code = False
    else:
        print('Oops! You must have typed something wrong!')
