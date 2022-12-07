class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.directories = {}
        self.files = {}

    def add_dir(self, name):
        x = Dir(name, self)
        self.directories[name] = x
        return x

    def add_file(self, name, size):
        self.files[name] = File(name, size)

    def _file_size(self):
        result = 0
        for file in self.files.values():
            result += file.size
        return result

    def cd(self, name):
        if name == '..':
            return self.parent
        else:
            return self.directories[name]

    def size(self):
        result = 0
        curr = self._file_size()
        for directory in self.directories.values():
            result += directory.size()
        if curr:
            result += curr
        return result


ROOT = '/'


def build_directory():
    tree = Dir('', None)
    pointer = tree
    dirs = [tree]
    tree.add_dir(ROOT)
    with open('data.txt', 'r') as f:
        for x in f.readlines():
            line = x.strip()
            if line.startswith("$"):
                cmd = line[2:].strip()
                if cmd.startswith('cd'):
                    pointer = pointer.cd(cmd.split(' ')[1])
            else:
                if line.startswith('dir'):
                    cmd, name = line.split(' ')
                    x = pointer.add_dir(name)
                    dirs.append(x)
                else:
                    size, name = line.split(' ')
                    pointer.add_file(name, int(size))
    return dirs


def part1():
    result = 0
    dirs = build_directory()
    for directory in dirs:
        size = directory.size()
        if size <= 100000:
            result += size
    return result


def part2():
    dirs = build_directory()
    dirs.sort(key=lambda x: x.size(), reverse=True)
    root = dirs[0]
    TOTAL = 70000000
    MIN = 30000000
    UNUSED = TOTAL - root.size()
    candidate = root
    dirs = dirs[1:]
    for directory in dirs:
        if directory.size() + UNUSED > MIN:
            candidate = directory
    else:
        return candidate.size()


if __name__ == '__main__':
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
