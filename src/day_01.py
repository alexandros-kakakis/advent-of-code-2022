
with open('../data/puzzle_input_day_01.txt') as f:
    lines = f.read().split('\n\n')

totals = [sum([int(i) for i in line.splitlines()]) for line in lines]
totals.sort(reverse=True)

print('Part One:', totals[0])
print('Part Two:', sum(totals[:3]))
