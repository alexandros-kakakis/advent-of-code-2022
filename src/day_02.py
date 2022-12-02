class Game:
    def __init__(self):
        self.score = 0

    def play(self, opponent_pick, my_pick):
        if my_pick == 'X':
            self.score += 1 + 6 * (opponent_pick == 'C') + 3 * (opponent_pick == 'A')
        elif my_pick == 'Y':
            self.score += 2 + 6 * (opponent_pick == 'A') + 3 * (opponent_pick == 'B')
        elif my_pick == 'Z':
            self.score += 3 + 6 * (opponent_pick == 'B') + 3 * (opponent_pick == 'C')

    def play_part_two(self, opponent_pick, expected_result):
        if expected_result == 'X':
            if opponent_pick == 'A':
                self.play(opponent_pick, 'Z')
            elif opponent_pick == 'B':
                self.play(opponent_pick, 'X')
            elif opponent_pick == 'C':
                self.play(opponent_pick, 'Y')

        elif expected_result == 'Y':
            if opponent_pick == 'A':
                self.play(opponent_pick, 'X')
            elif opponent_pick == 'B':
                self.play(opponent_pick, 'Y')
            elif opponent_pick == 'C':
                self.play(opponent_pick, 'Z')

        elif expected_result == 'Z':
            if opponent_pick == 'A':
                self.play(opponent_pick, 'Y')
            elif opponent_pick == 'B':
                self.play(opponent_pick, 'Z')
            elif opponent_pick == 'C':
                self.play(opponent_pick, 'X')


with open('../data/puzzle_input_day_02.txt') as f:
    lines = f.read().splitlines()


game = Game()
for line in lines:
    opponent_pick, my_pick = line.split()
    game.play(opponent_pick, my_pick)

print('Part One:', game.score)


game = Game()
for line in lines:
    opponent_pick, expected_result = line.split()
    game.play_part_two(opponent_pick, expected_result)

print('Part Two:', game.score)
