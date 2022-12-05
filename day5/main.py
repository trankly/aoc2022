def build_stacks(line, counter, crate, stack, stacks):
    for el in line:
        if el.isdigit():
            pass
        elif counter < 3:
            crate = crate + el
            counter += 1
        else:
            counter = 0
            if len(stacks) < stack:
                stacks.append([])

            if crate.strip():
                crate = crate.replace('[', '').replace(']', '')
                if len(stacks) > stack:
                    stacks[stack].insert(0, crate)
                else:
                    stacks.append([crate])
            stack += 1
            crate = ""


def part1():
    with open('data.txt', 'r') as f:
        result = ""
        stacks = []
        counter = 0
        stack = 0
        crate = ""
        for line in f.readlines():
            if line.startswith('move'):
                s, f, t = [int(x) for x in line.split() if x.isdigit()]
                while s > 0:
                    mv = stacks[f - 1].pop()
                    stacks[t - 1].append(mv)
                    s -= 1
            else:
                build_stacks(line, counter, crate, stack, stacks)
                stack = 0
        for s in stacks:
            result += s.pop()
        return result


def part2():
    with open('data.txt', 'r') as f:
        result = ""
        stacks = []
        counter = 0
        stack = 0
        crate = ""
        for line in f.readlines():
            if line.startswith('move'):
                s, f, t = [int(x) for x in line.split() if x.isdigit()]
                v = stacks[f - 1]
                slc = v[len(v) - s:]
                stacks[t - 1].extend(slc)
                while s > 0:
                    stacks[f - 1].pop()
                    s -= 1
            else:
                build_stacks(line, counter, crate, stack, stacks)
                stack = 0
        for s in stacks:
            result += s.pop()
        return result


if __name__ == '__main__':
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
