def prep_range(pair):
    return [int(x) for x in pair.split('-')]


def get_range(pair):
    a, b = prep_range(pair)
    return list(range(a, b + 1))


def part1():
    total = 0
    with open('data.txt', 'r') as f:
        for pairs in f.readlines():
            left, right = pairs.strip().split(',')
            a = get_range(left)
            b = get_range(right)
            overlap = set(a).intersection(set(b))
            if len(overlap) == len(a) or len(overlap) == len(b):
                total += 1
    return total


def part2():
    total = 0
    with open('data.txt', 'r') as f:
        for pairs in f.readlines():
            left, right = pairs.strip().split(',')
            a = get_range(left)
            b = get_range(right)
            overlap = set(a).intersection(set(b))
            if len(overlap) > 0:
                total += 1
    return total


if __name__ == '__main__':
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
