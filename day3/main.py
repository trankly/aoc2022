alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def priority(letter):
    return alpha.index(letter) + 1


def compartmentalize(rucksack):
    total_items = len(rucksack)
    return rucksack[slice(0, total_items // 2)], rucksack[slice(total_items // 2, total_items)]


def part1():
    total = 0
    with open('data.txt', 'r') as f:
        for rucksack in f.readlines():
            left, right = compartmentalize(rucksack.strip())
            left_items = {*left}
            right_items = {*right}
            both = left_items.intersection(right_items)
            for item in both:
                total += priority(item)
    return total


def score_badge(group):
    a, b, c = group
    return priority(list({*a}.intersection({*b}, {*c}))[0])


def part2():
    total = 0
    group = []
    with open('data.txt', 'r') as f:
        for rucksack in f.readlines():
            if len(group) < 3:
                group.append(rucksack.strip())
            else:
                total += score_badge(group)
                group = [rucksack.strip()]
        total += score_badge(group)
    return total


if __name__ == '__main__':
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
