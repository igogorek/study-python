def unique_in_order(seq):
    return [seq[i] for i in xrange(0, len(seq)) if i == 0 or seq[i] != seq[i-1]]


print unique_in_order('AAAdDDsssSS')