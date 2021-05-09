code = True
while code == True:
    print('Would you like to encrpyt or decrypt?')
    print('E = Encrpyt')
    print('D = Decrypt')
    print('Q = Quit')
    choose = input('Choose: ')
    choose = choose.upper()
    if choose == 'E':
        word = input("Enter a message: ")
        word_list = list(word)
        encrypt_word = []
        def printencrypt():
            print('Your encrypted word is: ' + ''.join(encrypt_word))
        shift = int(input("Enter a shift: "))
        for i in range(len(word_list)):
            letter = word_list[i]
            if letter.islower():
                cletter = chr((ord(letter) - ord("a") + shift) % 26 + ord("a"))
                encrypt_word.append(cletter)
            elif letter.isupper():
                cletter = chr((ord(letter) - ord("A") + shift) % 26 + ord("A"))
                encrypt_word.append(cletter)
            else:
                cletter = letter
                encrypt_word.append(cletter)
        printencrypt()
    elif choose == 'D':
        word = input("Enter a encrypted word: ")
        word_list = list(word)
        shift = input("Enter a word in the message: ")
        decrypt = True
        while decrypt == True:
            for i in range(1,27):
                decrypt_word = []
                shift_number = i
                for s in range(len(word_list)):
                    letter = word_list[s]
                    if letter.islower():
                        cletter = chr((ord(letter) - ord("a") - shift_number) % 26 + ord("a"))
                        decrypt_word.append(cletter)
                    elif letter.isupper():
                        cletter = chr((ord(letter) - ord("A") - shift_number) % 26 + ord("A"))
                        decrypt_word.append(cletter)
                    else:
                        cletter = letter
                        decrypt_word.append(cletter)
                check = ''.join(decrypt_word)
                if shift in check:
                    print('Your decrypted message is: ' + ''.join(decrypt_word))
                    decrypt = False
    elif choose == 'Q':
        code = False
    else:
        print('Oops! You must have typed something wrong!')
