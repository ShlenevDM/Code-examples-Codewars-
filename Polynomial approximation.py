# Find the nth Term of a Sequence
# https://www.codewars.com/kata/60f9f0145a54f500107ae29b/train/python
# numpy is blocked in this kata


def solve_sequence(seq):
    n_max = len(seq)
    if n_max == 0:
        return lambda n: 0
    elif n_max == 1:
        return lambda n: seq[0]
    for k in range(n_max):
        pass

