import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v',
            'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(message_, shiftkey_):
    encrypted_message = ""
    for item in message_:
        position = alphabet.index(item)
        new_position = position + shiftkey_
        while new_position > 26:
            new_position -= 26
        encrypted_message += alphabet[new_position]
    return encrypted_message


def decrypt(message_, shiftkey_):
    decrypted_message = ""
    for item in message_:
        position = alphabet.index(item)
        new_position = position - shiftkey_

        while new_position < 0:
            new_position += 26
        decrypted_message += alphabet[new_position]
    return  decrypted_message

is_gameOn = True
print(art.logo)
while is_gameOn:
    type = input("To encrypt type 'encode' and decrypt type 'decode': ").lower()

    if type == "encode":
        message = input("enter your message: ").lower()
        shiftkey = int(input("enter the shift key: "))
        print(encrypt(message, shiftkey))
    #twlfsnefynts
    elif type == "decode":
        message = input("enter your message: ").lower()
        shiftkey = int(input("enter the shift key: "))
        print(decrypt(message, shiftkey))
    else:
        print("oops try again!!")

    goOn = input("you want to end type 'no' else press enter : ").lower()
    if goOn == "no":
        is_gameOn = False
        print("Feel free to come Back...")