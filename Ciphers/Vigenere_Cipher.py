import os
os.system('cls')
code = True
while code:
    name = input('What is your name: ')
    print('Hello ' + name + ', hope you are having a great day!!')
    choose = input('Which one would you like to do first?\n1 = Encrypt\n2 = Decrypt\nQ = Quit\nChoice: ')
    if choose == '1':  
        first = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(26)))
        last = dict(zip(range(26), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        message = input('Enter message to be encrypted(no symbols): ')
        message = message.upper()
        key = input('Enter the key to be used(no symbols): ')
        key = key.upper().replace(' ','')
        lm = len(message)
        lk = len(key)
        spaces = [i for i in range(lm) if message[i]==' ']
        message2 = message.replace(' ','')
        lm = len(message2)
        if lk > lm:
            key = key[:lm]
        else:
            for i in range(lk,lm):
                key += key[i%lk]
        cipher = [last[(first[message2[i]] + first[key[i]])%26] for i in range(lm)]
        for i in spaces:
            cipher.insert(i,' ')
        cipher = ''.join(cipher)
        print('Original message: ' + message)
        print('Encrypted message: ' + cipher)
    elif choose == '2':  
        first = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(26)))
        last = dict(zip(range(26), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        message = input('Enter message to be decrypted(no symbols): ')
        message = message.upper()
        key = input('Enter the key to be used(no symbols): ')
        key = key.upper().replace(' ','')
        lm = len(message)
        lk = len(key)
        spaces = [i for i in range(lm) if message[i]==' ']
        message2 = message.replace(' ','')
        lm = len(message2)
        if lk > lm:
            key = key[:lm]
        else:
            for i in range(lk,lm):
                key += key[i%lk]
        plain = [last[(first[message2[i]] - first[key[i]])%26] for i in range(lm)]
        for i in spaces:
            plain.insert(i,' ')
        plain = ''.join(plain)
        print('Encrypted message: ' + message)
        print('Decrypted message: ' + plain)
    elif choose == 'Q':
        code = False
    else:
        print('You must have typed something wrong!!\nPlease try again!!')
