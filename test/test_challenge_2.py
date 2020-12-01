import unittest

from util.util import decode_hex, xor_bytes


class MyTestCase(unittest.TestCase):
    def test_xor(self):
        input1 = decode_hex("1c0111001f010100061a024b53535009181c")
        input2 = decode_hex("686974207468652062756c6c277320657965")
        result = decode_hex("746865206b696420646f6e277420706c6179")
        assert xor_bytes(input1, input2) == result
