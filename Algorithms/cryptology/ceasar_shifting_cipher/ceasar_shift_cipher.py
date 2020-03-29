'''
The Ceasar cipher is one of the simplest and one of the earliest known ciphers.
It is a type of substitution cipher that 'shifts' a letter by a fixed amount in the alphabet.

For example with a shift = 3:
a -> d
b -> e
.
.
.
z -> c

Programmed by Aladdin Persson <aladdin.persson at hotmail dot com>
*   2019-11-07 Initial programming

'''

# This alphabet is of 27 letters since I included a space, but normally it is of 26 letters.
# If you wish to include more letters you need to expand the alphabet used. For example you cannot use '!', '@' now.
alphabet = 'abcdefghijklmnopqrstuvwxyz '
letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))

def encrypt(message, shift=3):
    cipher = ''

    for letter in message:
        number = (letter_to_index[letter] + shift) % len(letter_to_index)
        letter = index_to_letter[number]
        cipher += letter

    return cipher

def decrypt(cipher, shift=3):
    decrypted = ''

    for letter in cipher:
        number = (letter_to_index[letter] - shift) % len(letter_to_index)
        letter = index_to_letter[number]
        decrypted += letter

    return decrypted

# def main():
#     message = 'attackatnoon'
#     cipher = encrypt(message, shift=3)
#     decrypted = decrypt(cipher, shift=3)
#
#     print('Original message: ' + message)
#     print('Encrypted message: ' + cipher)
#     print('Decrypted message: ' + decrypted)
#
# main()