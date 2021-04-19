from __future__ import division

# sqrt2f = 0.4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727
# no big float, so use sqrt2f * 10**100 // 10**100
sqrt2f100 = 4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727
ten100 = 10**100

'''
see https://math.stackexchange.com/questions/2052179/how-to-find-sum-i-1n-left-lfloor-i-sqrt2-right-rfloor-a001951-a-beatty-s
'''
def beatty_seq_sum(n):
    # m = floor((sqrt2 - 1)*n)
    # s(sqrt2,n) = (n + m) * (n + m + 1) // 2 - m * (m + 1) - s(sqrt2, m)
    if n == 0:
        return 0
    m = sqrt2f100 * n // ten100
    return (n + m) * (n + m + 1) // 2 - m * (m + 1) - beatty_seq_sum(m)


def solution(s):
    n = int(s)
    ret = beatty_seq_sum(n)
    return str(ret)


if __name__ == '__main__':
    print(solution('77'))
    # 4208
    print(solution('5'))
    # 19
