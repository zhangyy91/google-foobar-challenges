def is_loop(a, b):
    n = a + b
    while n % 2 == 0:
        n /= 2
    return a % n != 0


def select_fewest(mapping, keys):
    ret = None
    l = 101
    for i in keys:
        ll = len(mapping[i])
        if ll < l:
            ret = i
            l = ll
    return ret


def remove(mapping, key):
    for v in mapping[key]:
        mapping[v].remove(key)
    mapping.pop(key)


def greed_solve(mapping):
    # similar to topological sort
    ret = 0
    while len(mapping) > 0:
        # select node with fewest edges
        i = select_fewest(mapping, mapping.keys())
        # select neighbor with fewest edges
        j = select_fewest(mapping, mapping[i])
        remove(mapping, i)
        if j is not None:
            remove(mapping, j)
        else:
            ret += 1
    return ret


def solution(banana_list):
    n = len(banana_list)
    mapping = {}
    for i in range(n):
        mapping[i] = set()
    for i in range(n):
        for j in range(i + 1, n):
            if is_loop(banana_list[i], banana_list[j]):
                mapping[i].add(j)
                mapping[j].add(i)
    return greed_solve(mapping)


if __name__ == '__main__':
    print(solution([1, 7, 3, 21, 13, 19]))
    # 0
    print(solution([1, 1]))
    # 2
