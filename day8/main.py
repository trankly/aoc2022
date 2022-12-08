import copy


def transpose(grid):
    return [list(sublist) for sublist in list(zip(*grid))]


def chop(grid):
    first = len(grid[0])
    grid = grid[1:]
    last = len(grid.pop())
    return grid, first + last


def chop_all(grid):
    grid, x = chop(grid)
    grid, y = chop(transpose(grid))
    return transpose(grid), x + y


def is_visible(row, index):
    tree = row[index]
    right = max(row[index + 1:])
    left = max(row[:index])
    return tree > right or tree > left


def all_visible(grid, visible):
    for i1, row in enumerate(grid):
        for i2, tree in enumerate(row):
            if i1 == 0 or i2 == 0 or i1 == len(grid) - 1 or i2 == len(row) - 1:
                visible[i1][i2] = 1
            elif 0 < i1 < len(grid) and 0 < i2 < len(row) - 1:
                if is_visible(row, i2):
                    visible[i1][i2] = 1
    return visible


def make_grid():
    grid = []
    with open('data.txt', 'r') as f:
        for row in f.readlines():
            grid_row = []
            for tree in row.strip():
                grid_row.append(int(tree))
            grid.append(grid_row)
    return grid


def get_zeros(grid, val=0):
    template = [val] * len(grid[0])
    zeros = []
    for x in grid:
        zeros.append(copy.deepcopy(template))
    return zeros


def scenic_score(row, index, score):
    result = score
    right = row[index + 1:]
    tree = row[index]
    if right:
        view = []
        for x in right:
            if x < tree:
                view.append(x)
            else:
                view.append(x)
                break
        result *= len(view)
    else:
        result = 0

    left = row[:index]
    if left:
        view = []
        for x in list(reversed(left)):
            if x < tree:
                view.append(x)
            else:
                view.append(x)
                break
        result *= len(view)
    else:
        result = 0
    return result


def scenic(grid, scores):
    for i1, row in enumerate(grid):
        for i2, tree in enumerate(row):
            score = scenic_score(row, i2, scores[i1][i2])
            scores[i1][i2] = score

    return scores


def part1():
    result = 0
    grid = make_grid()
    internal, edge_count = chop_all(grid)
    visible = get_zeros(grid)
    visible = all_visible(grid, visible)
    visible = all_visible(transpose(grid), transpose(visible))
    for x in visible:
        for y in x:
            result += y

    return result


def part2():
    grid = make_grid()
    scores = get_zeros(grid, val=1)
    scores = scenic(grid, scores)
    scores = scenic(transpose(grid), transpose(scores))
    result = 0
    for row in scores:
        for tree in row:
            if tree > result:
                result = tree
    return result


if __name__ == '__main__':
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
