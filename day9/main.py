import math


def diagonal(h, t):
    if h[0] != t[0] and h[1] != t[1]:
        d = math.sqrt((h[1] - t[1]) ** 2 + (h[0] - t[0]) ** 2)
        if d > 2:
            if h[0] > t[0]:
                x = 'R'
            else:
                x = 'L'
            if h[1] > t[1]:
                y = 'U'
            else:
                y = 'D'
            return x, y
    else:
        return None


def straight(h, t):
    if h[0] == t[0] or h[1] == t[1]:
        if h[0] == t[0] and h[1] == t[1]:
            return None
        elif h[0] == t[0]:
            distance = h[1] - t[1]
            if abs(distance) > 1:
                if distance < 0:
                    direction = 'D'
                else:
                    direction = 'U'
                return direction
        elif h[1] == t[1]:
            distance = h[0] - t[0]
            if abs(distance) > 1:
                if distance < 0:
                    direction = 'L'
                else:
                    direction = 'R'
                return direction


def move(p, direction, distance):
    if direction == 'R':
        p[0] += distance
    elif direction == 'L':
        p[0] -= distance
    elif direction == 'U':
        p[1] += distance
    elif direction == 'D':
        p[1] -= distance
    return p


def follow(h, t):
    t_d = straight(h, t)
    diag = diagonal(h, t)
    if t_d:
        move(t, t_d, 1)
    elif diag:
        t_x, t_y = diag
        move(t, t_x, 1)
        move(t, t_y, 1)


def part1():
    h_position = [0, 0]
    t_position = [0, 0]
    visited = set()
    with open('data.txt', 'r') as f:
        for m in f.readlines():
            direction, distance = m.strip().split()
            distance = int(distance)
            count = 0
            while count < distance:
                move(h_position, direction, 1)
                follow(h_position, t_position)
                count += 1
                visited.add(tuple(t_position))
    return len(visited)


def part2():
    head = [0, 0]
    positions = [[0, 0] for _ in range(8)]
    tail = [0, 0]
    positions.append(tail)
    visited = set()
    with open('data.txt', 'r') as f:
        for m in f.readlines():
            direction, distance = m.strip().split()
            distance = int(distance)
            count = 0
            while count < distance:
                move(head, direction, 1)
                last = head
                for knot in positions:
                    follow(last, knot)
                    last = knot
                follow(knot, tail)
                count += 1
                visited.add(tuple(tail))
    print(positions)
    return len(visited)
    pass


if __name__ == '__main__':
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
