import operator
from base64 import b64encode
from string import ascii_lowercase


def hex_to_b64(string):
    return encode_b64(decode_hex(string))


def decode_hex(string):
    return bytes.fromhex(string)


def encode_b64(b):
    return b64encode(b).decode()


def xor_bytes(b, c):
    return bytes([_b ^ _c for _b, _c in zip(b, c)])


def letter_frequency_score(string):
    frequencies = {}
    filtered_string = filter(lambda c: c in ascii_lowercase, string.lower())
    for char in filtered_string:
        curr_freq = frequencies.setdefault(char, 0)
        frequencies[char] = curr_freq + 1
    sorted_frequencies = [char for (char, freq) in sorted(frequencies.items(), key=operator.itemgetter(1))]
    lowest_5 = set(sorted_frequencies[:5])
    highest_5 = set(sorted_frequencies[-5:])
    score = len(lowest_5 & set('shrdlu')) + len(highest_5 & set('etaoin'))
    return score
