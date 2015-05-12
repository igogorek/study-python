__author__ = 'igogor'
from itertools import chain, combinations

def decompose(n):
    numbers = [num for num in xrange(1, n)]
    sets = [list(val)[::-1] for val in chain.from_iterable(combinations(numbers, r) for r in xrange(1, len(numbers)))]
    for set in sorted(sets, reverse=True):
        if sum([num**2 for num in set]) == n**2:
           return set[::-1]
    return None

print decompose(11)


