# Import folder where sorting algorithms
import sys
import unittest

# For importing from different folders
# OBS: This is supposed to be done with automated testing, hence relative to folder we want to import from
sys.path.append('Algorithms/cryptology/ceasar_shifting_cipher')

# If run from local:
#sys.path.append('../../Algorithms/cryptology/ceasar_shifting_cipher')

from ceasar_shift_cipher import encrypt, decrypt

# Note this is not robust.. but im trying to make it a habit to make some tests.
# Some are better than nothing. But these are not complete at all.
class test_ceasar_cipher(unittest.TestCase):

    def setUp(self):
        # test cases we wish to run
        self.message1 = 'abc'
        self.shift1 = 3
        self.correct_encrypt1 = 'def'

        self.message2 = 'xyz '
        self.shift2 = 1
        self.correct_encrypt2 = 'yz a'


    def test_encryption_message1(self):
        encrypted_message1 = encrypt(self.message1, self.shift1)
        self.assertEqual(encrypted_message1, self.correct_encrypt1)

    def test_decryption_message1(self):
        decrypted_message1 = decrypt(self.correct_encrypt1, self.shift1)
        self.assertEqual(decrypted_message1, self.message1)

    def test_encryption_message2(self):
        encrypted_message2 = encrypt(self.message2, self.shift2)
        self.assertEqual(encrypted_message2, self.correct_encrypt2)

    def test_decryption_message2(self):
        decrypted_message2 = decrypt(self.correct_encrypt2, self.shift2)
        self.assertEqual(decrypted_message2, self.message2)

if __name__ == '__main__':
    print("Running ceasar cipher tests:")
    unittest.main()