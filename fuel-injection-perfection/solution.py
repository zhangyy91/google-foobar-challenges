def solution(n):
    l = []
    n = int(n)
    while n != 0:
        b = n % 2
        n //= 2
        if len(l) == 0 or l[-1][0] != b:
            l.append([b, 1])
        else:
            l[-1][1] += 1
    ret = 0
    last = len(l) - 1
    for i in range(len(l)):
        if l[i][0] == 0:
            ret += l[i][1]
        else:
            if i == last:
                if l[i][1] == 1:
                    pass
                elif l[i][1] == 2:
                    ret += 2
                else:
                    ret += l[i][1] + 1
            else:
                if l[i][1] == 1:
                    ret += 2
                else:
                    ret += l[i][1] + 1
                    l[i + 1][1] -= 1
                    if l[i + 1][1] == 0:
                        l[i + 2][1] += 1
                    else:
                        ret += 2
    return ret

if __name__ == '__main__':
    test = [4, 15, 11, 13, 27, 32, 123]
    for v in test:
        print("{} => {}".format(v, solution(str(v))))