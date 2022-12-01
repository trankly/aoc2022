def clean(num):
    return int(num.replace("\n", ""))


def part1():
    elf = 0
    elfs = {}
    with open('./data.txt', 'r') as f:
        for line in f.readlines():
            if line == "\n":
                elf += 1
            else:
                if elf in elfs:
                    elfs[elf] += clean(line)
                else:
                    elfs[elf] = clean(line)
    return sorted(list(elfs.values()), reverse=True)


if __name__ == "__main__":
    print("Part 1: ", part1()[0])
    print("Part 2: ", part1()[0] + part1()[1] + part1()[2])

