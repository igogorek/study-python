import time

def gimme(inputArray):
    max_index = inputArray.index(max(inputArray))
    min_index = inputArray.index(min(inputArray))
    for i in xrange(len(inputArray)):
        if i not in [max_index, min_index]:
            return i

def one_line(list):
    return list.index(sorted(list)[1])

start = time.time()
for i in xrange(100000):
    gimme([-54, -3, 22])
print 'time %s' % (time.time() - start)


start = time.time()
for i in xrange(100000):
    one_line([-54, -3, 22])
print 'time %s' % (time.time() - start)


