from __future__ import division
from fractions import Fraction, gcd


def mmat(m, n, v=0.):
    return [[v] * n for _ in range(m)]


def midentity(n):
    m = mmat(n, n)
    for i in range(n):
        m[i][i] = 1.
    return m


def mshape(m):
    return len(m), len(m[0])


def mlike(m):
    r, c = mshape(m)
    return mmat(r, c)


def mcopy(m):
    mm = mlike(m)
    r, c = mshape(mm)
    for i in range(r):
        for j in range(c):
            mm[i][j] = m[i][j]
    return mm


def mdot(m1, m2):
    rows1, cols1 = mshape(m1)
    rows2, cols2 = mshape(m2)
    if cols1 != rows2:
        raise Exception("illegal shapes")
    ret = mmat(rows1, cols2)
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                ret[i][j] += m1[i][k] * m2[k][j]
    return ret


def msub(m1, m2, in_place=False):
    r1, c1 = mshape(m1)
    r2, c2 = mshape(m2)
    if r1 != r2 or c1 != c2:
        raise Exception("illegal shapes")
    m = m1 if in_place else mcopy(m1)
    for i in range(r1):
        for j in range(c1):
            m[i][j] -= m2[i][j]
    return m


def mtrans(m):
    return list(map(list, zip(*m)))


def mdet(m):
    n, c = mshape(m)
    if n != c:
        raise Exception("illegal shape")
    if n == 1:
        return m[0][0]
    if n == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    ret = 0
    for j in range(n):
        ret += (-1)**j * m[0][j] * mdet(mminor(m, 0, j))
    return ret


def mminor(m, i, j):
    r, c = mshape(m)
    mm = []
    for ii, row in enumerate(m):
        if ii != i:
            mm.append(row[:j] + row[j+1:])
    return mm


def minv(m):
    d = mdet(m)
    cof = []
    n, _ = mshape(m)
    for i in range(n):
        crow = []
        for j in range(n):
            crow.append((-1)**(i+j) * mdet(mminor(m, i, j)) / d)
        cof.append(crow)
    return mtrans(cof)


def lcm(a, b):
    return abs(a*b) // gcd(a, b)


def to_std_qr(m):
    absorbs = []
    for i, row in enumerate(m):
        if sum(row) == 0:
            absorbs.append(i)
    q = []
    r = []
    for i, row in enumerate(m):
        if i not in absorbs:
            s = sum(row)
            qrow = []
            rrow = []
            for j, freq in enumerate(row):
                if j not in absorbs:
                    qrow.append(freq / s)
                else:
                    rrow.append(freq / s)
            q.append(qrow)
            r.append(rrow)
    return q, r


def to_fracs(ll):
    l = 1
    fracs = []
    for n in ll:
        f = Fraction(n).limit_denominator()
        l = lcm(l, f.denominator)
        fracs.append(f)
    ret = []
    for f in fracs:
        ret.append((f * l).numerator)
    ret.append(l)
    return ret


def solution2(m):
    # absorbing markov chain
    # standard form
    # p   = [[q, r],
    #       [0, i]]
    # p^n = [[0, (i-q)^-1 * r],
    #        [0, i]]
    #       lim n -> inf
    import numpy as np
    q, r = to_std_qr(m)
    q = np.array(q)
    r = np.array(r)
    inv = np.linalg.inv(np.subtract(np.identity(len(q)), q))
    probs = np.dot(inv, r)
    ret = to_fracs(probs[0])
    return ret

def solution(m):
    if len(m) == 1:
        return [1, 1]
    q, r = to_std_qr(m)
    i = midentity(len(q))
    iq = msub(i, q)
    inv = minv(iq)
    probs = mdot(inv, r)
    ret = to_fracs(probs[0])
    return ret


if __name__ == '__main__':
    case1 = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [
             0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    print(solution(case1))
    # -> [7, 6, 8, 21]

    case2 = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [
             0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    print(solution(case2))
    # -> [0, 3, 2, 9, 14]
