from __future__ import division
IMPOSSIBLE = 'impossible'


def solution(x, y):
    # f(m, f) -> (m, m + f) or (m + f, f)
    x = int(x)
    y = int(y)
    ret = 0
    while x != 1 and y != 1 and x != 0 and y != 0:
        if x < y:
            x, y = y, x
        t = x // y
        d = x - t * y
        x, y = y, d
        ret += t
    if x == 1:
        return str(ret + y - 1)
    if y == 1:
        return str(ret + x - 1)
    else:
        return IMPOSSIBLE


if __name__ == '__main__':
    case1 = ['2', '1']
    print(solution(case1[0], case1[1]))
    # > 1
    case2 = ['4', '7']
    print(solution(case2[0], case2[1]))
    # > 4
    case3 = ['2', '4']
    print(solution(case3[0], case3[1]))
    # > impossible
