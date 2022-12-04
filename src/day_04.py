import re

with open('../data/puzzle_input_day_04.txt') as f:
    lines = f.read().splitlines()

lines = [re.findall(r'(\d+)', line) for line in lines]
lines = [[int(i) for i in line] for line in lines]

range_pairs = [
    (set(range(line[0], line[1]+1)), set(range(line[2], line[3]+1))) for line in lines
]

fully_overlapping = [min(len(r[0] - r[1]), len(r[1] - r[0])) == 0 for r in range_pairs]
partially_overlapping = [len(r[0] & r[1]) > 0 for r in range_pairs]

print('Part One:', sum(fully_overlapping))
print('Part Two:', sum(partially_overlapping))
