# return a list of tuples sorted by frequency with
# the most frequent letter first. Any letters with the
# same frequency are ordered alphabetically
from collections import defaultdict

def letter_frequency(text):

    letter_dict = defaultdict(int)
    for letter in [symbol.lower() for symbol in text if symbol.isalpha()]:
        letter_dict[letter] += 1

    return sorted(letter_dict.items(), key=lambda x: (-x[1], x[0]))

print letter_frequency("As long as I'm learning something, I figure I'm OK - it's a decent day.")