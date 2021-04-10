from __future__ import division
from fractions import gcd


def sign(x):
    if x > 0:
        return 1
    else:
        return -1


def mirror(tx, ty, w, h, m, n):
    x = tx + m // 2 * 2 * w + m % 2 * 2 * (w - tx)
    y = ty + n // 2 * 2 * h + n % 2 * 2 * (h - ty)
    return x, y


def dist(x1, y1, x2, y2):
    return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)


def detect(w, h, x, y, tx, ty, d, me, ne):
    d = d * d
    dx = sign(me)
    dy = sign(ne)
    ret = {} # direction => distance
    for m in range(0, me, dx):
        nx, ny = mirror(tx, ty, w, h, m, 0)
        if dist(nx, ny, x, y) > d:
            break
        for n in range(0, ne, dy):
            nx, ny = mirror(tx, ty, w, h, m, n)
            dd = dist(nx, ny, x, y)
            if dd > d:
                break
            vx, vy = nx - x, ny - y
            if vx == 0 and vy == 0:
                continue
            g = gcd(abs(vx), abs(vy)) # fractions.gcd may return negative number
            vx, vy = vx // g, vy // g
            if (vx, vy) not in ret:
                ret[(vx, vy)] = dd
    return ret


def detect2(w, h, x, y, tx, ty, d, me, ne):
    ba = detect(w, h, x, y, x, y, d, me, ne)
    a = detect(w, h, x, y, tx, ty, d, me, ne)
    ret = set()
    for (x, y), dd in a.items():
        if (x, y) not in ba or (x, y) in ba and dd < ba[(x, y)]:
            ret.add((x, y))
    return ret


def solution(dimensions, your_position, trainer_position, distance):
    # reflect both you and the trainer into the mirror world
    # if the beam in a direction hits both you and the trainer, compare the distance
    w, h = dimensions
    x, y = your_position
    tx, ty = trainer_position
    d = distance
    md = 10001
    r1 = detect2(w, h, x, y, tx, ty, d, md, md)
    r2 = detect2(w, h, x, y, tx, ty, d, md, -md)
    r3 = detect2(w, h, x, y, tx, ty, d, -md, -md)
    r4 = detect2(w, h, x, y, tx, ty, d, -md, md)

    ds = r1.union(r2, r3, r4)
    return len(ds)


if __name__ == '__main__':
    print(solution([3, 2], [1, 1], [2, 1], 4))
    # 7, [1, 0], [1, 2], [1, -2], [3, 2], [3, -2], [-3, 2], and [-3, -2]
    print(solution([300, 275], [150, 150], [185, 100], 500))
    # 9