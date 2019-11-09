alphabet = 'abcdefghijklmnopqrstuvxyz '

letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))

def encrypt(message, shift=3):
	cipher = ''

	for letter in message:
		number = (letter_to_index[letter] + shift) % len(alphabet)
		shifted_letter = index_to_letter[number]

		cipher += shifted_letter

	return cipher


def decrypt(cipher, shift=3):
	decrypted_message = ''

	for letter in cipher:
		number = (letter_to_index[letter] - shift) % len(alphabet)
		shifted_letter = index_to_letter[number]

		decrypted_message += shifted_letter

	return decrypted_message


def main():
	message = 'attack at noon'
	encrypted_message = encrypt(message, shift=3)
	decrypted_message = decrypt(encrypted_message, shift=3)

	print("Original message: " + message)
	print("Encrypted message: " + encrypted_message)
	print("Decrypted message: " + decrypted_message)


main()




