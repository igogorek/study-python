# return a list of tuples sorted by frequency with
# the most frequent letter first. Any letters with the
# same frequency are ordered alphabetically
from collections import Counter

def letter_frequency(text):

    return sorted(Counter(filter(str.isalpha, text.lower())).most_common(), key=lambda x: (-x[1], x[0]))

print letter_frequency("As long as I'm learning something, I figure I'm OK - it's a decent day.")