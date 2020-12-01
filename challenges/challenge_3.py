import itertools
import operator
import string

from util.util import xor_bytes, letter_frequency_score


def solve(input):
    candidates = []
    for char in string.ascii_lowercase:
        char_bytes = bytes(itertools.repeat(ord(char), len(input)))
        res = xor_bytes(input, char_bytes)
        candidate = str([chr(c) for c in res])
        candidates.append((letter_frequency_score(candidate), char, candidate))
    best = sorted(candidates, key=operator.itemgetter(0))
    [print(c) for c in best]
