def unique(integers):
    return [integers[i] for i in xrange(len(integers)) if integers[:i].count(integers[i]) == 0]