__author__ = 'igogor'
import time

# def decompose(n):
#     a_list = [n-1]
#     can_be_reduced = [0]
#     while len(can_be_reduced) > 0:
#         diff = n**2 - sum([m**2 for m in a_list])
#         if diff == 0 and len(a_list) == len(set(a_list)):
#             return a_list
#         elif diff > 0 and a_list[0] > 1:
#             a_list = [int(diff**0.5)] + a_list
#         else:
#             can_be_reduced = [index for index, element in enumerate(a_list) if element > index + 1]
#             if len(can_be_reduced) > 0:
#                 a_list[can_be_reduced[0]] -= 1
#                 if can_be_reduced[0] > 0:
#                     a_list = a_list[can_be_reduced[0]:]
#             else:
#                 return None


def decompose(n):
    def _recurse(s, i):
        if s < 0:
            return None
        if s == 0:
            return []
        for j in xrange(i-1, 0, -1):
            sub = _recurse(s - j**2, j)
            if sub is not None:
                return sub + [j]
    return _recurse(n**2, n)

start = time.time()

print decompose(11)
print decompose(50)
print decompose(4)
print decompose(7101)
print decompose(625)
print decompose(123456)
print decompose(1234567)
print decompose(7654321)

print "time: {}".format(time.time() - start)


