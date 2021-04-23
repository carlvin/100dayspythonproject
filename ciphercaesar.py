alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
finish = False
myint = True


def encrypt(name):
    cipher_text = ""
    for letter in name:
        position= alphabet.index(letter)
        print(position)
        new_position = position + shift
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(cipher_text)


def decrypt(name):
    pass


while not finish:
    direction = input('Type "encode" to encrypt, and "decode" to decrypt:\n')

    if direction == 'encode':
        while myint:
            # print(myint)
            try:
                shift = int(input('type the shift number:\n'))

                if type(shift) is int:
                    # print('type is int')
                    text = input('Type your message here \n')
                    myint = False

                else:
                    myint = False
            except ValueError as err:
                print('Enter numbers only')

    elif direction == 'decode':
        pass
        # decrypt(text)
    else:
        print("Follow given instructions")

    encrypt(text)