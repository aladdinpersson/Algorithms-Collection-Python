'''
Vigenère cipher is one of the simplest that employs a form of polyalphabetic substitution (each letter is assigned
more than one substitute).

It was first described in 1553 but took an entire three centuries to break it in 1863.

Weakness: If someone finds key length then this can be broken.

Programmed by Aladdin Persson <aladdin.persson at hotmail dot com>
*  2019-11-07 Initial programming

'''


alphabet = 'abcdefghijklmnopqrstuvwxyz '

letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))


def encrypt(message, key):
    encrypted = ''
    split_message = [message[i:i + len(key)] for i in range(0, len(message), len(key))]

    for each_split in split_message:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] + letter_to_index[key[i]]) % len(alphabet)
            encrypted += index_to_letter[number]
            i += 1

    return encrypted

def decrypt(cipher, key):
    decrypted = ''
    split_encrypted = [cipher[i:i + len(key)] for i in range(0, len(cipher), len(key))]

    for each_split in split_encrypted:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] - letter_to_index[key[i]]) % len(alphabet)
            decrypted += index_to_letter[number]
            i += 1

    return decrypted

def main():
    message = 'i loove peanuts'
    key = 'banana'
    encrypted_message = encrypt(message, key)
    decrypted_message = decrypt(encrypted_message, key)

    print('Original message: ' + message)
    print('Encrypted message: ' + encrypted_message)
    print('Decrypted message: ' + decrypted_message)

main()