# Should return triangle type:
#  0 : if triangle cannot be made with given sides
#  1 : acute triangle
#  2 : right triangle
#  3 : obtuse triangle


def triangle_type(a, b, c):
    s, m, l = sorted([a, b, c])
    if l >= m + s:
        return 0
    cmp_res = cmp(l ** 2, m ** 2 + s ** 2)
    if cmp_res < 0:
        return 1
    elif cmp_res == 0:
        return 2
    else:
        return 3
