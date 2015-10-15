# coding: utf-8
__author__ = 'igogor'

import hashlib


def hash_long(message):
    hash_ = long(hashlib.sha256(message).hexdigest(), base=16)
    print 'hash({}): {}'.format(message, hash_)
    return hash_


R_CONST = hash_long('asdfasdfasdfasdfasdf')
S_LIST = (hash_long('sdfdfalsdofiqjer'), hash_long('adfasdoqwer;lkqner;qwe'), hash_long('adlqoei;landlna'))
MESSAGES = ('11', '22', '33')
HASHES = [hash_long(message) for message in MESSAGES]
MAX_64 = long('f' * 64, base=16)


def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient * x, x
        y, lasty = lasty - quotient * y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)


def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m


def genmod():
    for n in range((R_CONST + 1), R_CONST + 1000, 1):
        # todo дят плейн вронг
        m1 = modinv(S_LIST[1] - S_LIST[0], n)
        m2 = modinv(S_LIST[2] - S_LIST[1], n)
        if m1 and m2 and m1 == m2:
            print 'n = {}'.format(n)
            yield n


def calc_k(s1, s2, z1, z2, n):
    k = ((z2 - z1) * modinv(s2 - s1, n)) % n
    print 'k = {}'.format(k)
    return k


def calc_dA(s, k, z, r, n):
    dA = ((s * k - z) * modinv(r, n)) % n
    print 'dA = {}'.format(dA)
    return dA


def calc_s(k, dA, z, r, n):
    s = (modinv(k, n) * (z + r * dA)) % n
    print 's = {}'.format(s)
    return s


def calc_r():
    raise NotImplementedError


def calc_main():
    for n in genmod():
        k = calc_k(s1=S_LIST[0], s2=S_LIST[1], z1=HASHES[0], z2=HASHES[1], n=n)
        dA = calc_dA(s=S_LIST[0], k=k, z=HASHES[0], r=R_CONST, n=n)
        if S_LIST[2] == calc_s(k=k, dA=dA, z=HASHES[2], r=R_CONST, n=n):
            s_getflag = calc_s(k=k, dA=dA, z=hash_long('GETFLAG'), r=R_CONST, n=n)
            print 'getflag s: {}'.format(s_getflag)
            print 'signature: (r={}, s={})'.format(hex(R_CONST), hex(s_getflag))
            break


calc_main()
