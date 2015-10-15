# coding: utf-8
__author__ = 'igogor'

import hashlib

def hash_long(message):
    hash_ = long(hashlib.sha256(message).hexdigit(), base=16)
    print 'hash(message): {}'.format(hash_)
    return hash_

R_CONST = 11
S_LIST = (11, 22, 33)
MESSAGES = ('11', '22', '33')
HASHES = [hash_long(message) for message in MESSAGES]
MAX_64 = long('f' * 64, base=16)


def modinv(num, n):
    return pow(num, n - 2, n)  # todo check


def genmod():
    for n in range(start=R_CONST + 1):
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
