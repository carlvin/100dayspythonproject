alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
finish = False


def crypto(name, shift, oper):
    cipher_text = ""
    for letter in name:
        position = alphabet.index(letter)
        # print(position)
        if oper == 'encrypt':
            new_position = sum([position,shift])
        else:
            new_position = position - shift

        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print (cipher_text)


def caesar():
    try:
        shift = int(input('type the shift number:\n'))

        if type(shift) is int:
            # print('type is int')
            text = input('Type your message here \n')

    except ValueError as err:
        print('Enter numbers only')

    return shift, text


while not finish:
    direction = input('Type "encode" to encrypt,"decode" to decrypt, and "quit" to exit:\n').lower()
    if direction == 'quit':
        break
    elif direction == 'encode':
        output = caesar()
        print(output[0])
        crypto(output[1], output[0], 'encrypt')
    elif direction == 'decode':
        output = caesar()
        crypto(output[1], output[0], 'decrypt')
