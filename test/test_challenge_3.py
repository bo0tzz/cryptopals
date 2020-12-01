import unittest

from challenges import challenge_3
from util.util import decode_hex


class MyTestCase(unittest.TestCase):
    def test_xor_cipher(self):
        input = decode_hex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
        challenge_3.solve(input)
