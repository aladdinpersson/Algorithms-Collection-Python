'''
Implementation of the famous one time pad / Vernam Cipher

In practice we need a way to generate random keys which I havn't included.

Programmed by Aladdin Persson <aladdin.persson at hotmail dot com>
*  2019-11-12 Initial programming

'''

def xor(s1,s2):
    xor_result = []

    for i in range(min(len(s1), len(s2))):
        xor_result.append(int(s1[i]) ^ int(s2[i])) # xor

    return xor_result

def encrypt(message, key):
    binary_message = ''
    binary_key = ''
    ciphered_text = ''

    for letter in message:
        binary_message += format(ord(letter), 'b')

    for letter in key:
        binary_key += format(ord(letter), 'b')

    cipher_binary = xor(binary_message, binary_key)

    return ''.join(str(e) for e in cipher_binary)

def decrypt(cipher_text, key):
    binary_key = ''
    decrypted_text = ''

    for letter in key:
        binary_key += format(ord(letter), 'b')


    binary_message = xor(cipher_text, binary_key)

    for i in range(0,len(binary_message),7):
        letter = ''.join(str(e) for e in binary_message[i:i+7])
        decrypted_text += chr(int(letter, 2))

    return decrypted_text


def main():
    message = 'cheesecake' # 'secret' message
    key = 'randomrandomrandom' #'random' key

    encrypted = encrypt(message, key)
    decrypted = decrypt(encrypted, key)

    print('Original message: ' + str(message))
    print('Encrypted message (in binary): ' + str(encrypted))
    print('Decrypted message: ' + str(decrypted))

if __name__ == '__main__':
    main()