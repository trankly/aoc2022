class Plays:
    ROCK = 'rock'
    PAPER = 'paper'
    SCISSORS = 'scissors'
    WIN = 6
    LOSS = 0
    DRAW = 3

    _scores = {
        ROCK: 1,
        PAPER: 2,
        SCISSORS: 3,
    }

    def winner(self, a, b):
        return a == self.ROCK and b == self.SCISSORS or \
               a == self.PAPER and b == self.ROCK or \
               a == self.SCISSORS and b == self.PAPER

    def score(self, a, b):
        a_score = self._scores[a]
        b_score = self._scores[b]

        if self.winner(a, b):
            return {
                'a': a_score + self.WIN,
                'b': b_score + self.LOSS,
            }
        elif self.winner(b, a):
            return {
                'a': a_score + self.LOSS,
                'b': b_score + self.WIN,
            }
        else:
            return {
                'a': a_score + self.DRAW,
                'b': b_score + self.DRAW,
            }

    def _invert_outcome(self, outcome):
        if outcome == self.WIN:
            return self.LOSS
        elif outcome == self.LOSS:
            return self.WIN
        else:
            return self.DRAW

    def _test(self, a, play, a_outcome, outcome):
        return a == play and self._invert_outcome(a_outcome) == outcome

    def revert_outcome(self, a, outcome):
        if self._test(a, self.ROCK, outcome, self.WIN) or self._test(a, self.PAPER, outcome, self.LOSS):
            return self.SCISSORS
        elif self._test(a, self.PAPER, outcome, self.WIN) or self._test(a, self.SCISSORS, outcome, self.LOSS):
            return self.ROCK
        elif self._test(a, self.SCISSORS, outcome, self.WIN) or self._test(a, self.ROCK, outcome, self.LOSS):
            return self.PAPER
        else:
            return a


def decode(play):
    plays = {
        'A': Plays.ROCK,
        'B': Plays.PAPER,
        'C': Plays.SCISSORS,
        'X': Plays.ROCK,
        'Y': Plays.PAPER,
        'Z': Plays.SCISSORS,
    }
    return plays[play]


def decode_outcome(outcome):
    outcomes = {
        'X': Plays.LOSS,
        'Y': Plays.DRAW,
        'Z': Plays.WIN,
    }
    return outcomes[outcome]


def part1():
    total = 0
    game = Plays()
    with open("./data.txt", 'r') as f:
        for play in f.readlines():
            a, b = play.strip().split()
            outcome = game.score(decode(a), decode(b))
            total += outcome['b']
    return total


def part2():
    total = 0
    game = Plays()
    with open("./data.txt", 'r') as f:
        for play in f.readlines():
            a, x = play.strip().split()
            b = game.revert_outcome(decode(a), decode_outcome(x))
            outcome = game.score(decode(a), b)
            total += outcome['b']

    return total


if __name__ == '__main__':
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
