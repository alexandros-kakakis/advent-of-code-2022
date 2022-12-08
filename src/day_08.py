import numpy as np

with open('../data/puzzle_input_day_08.txt') as f:
    lines = f.read().splitlines()

lines = [[int(i) for i in line] for line in lines]
quadcopter = np.matrix(lines)

grid_size = quadcopter.shape[0]
n_visible = 4 * grid_size - 4

for row in range(1, grid_size-1):
    for col in range(1, grid_size-1):

        smallest_blocking = np.min([
            quadcopter[0:row, col].max(),
            quadcopter[row + 1:, col].max(),
            quadcopter[row, 0:col].max(),
            quadcopter[row, col + 1:].max()
        ])

        if quadcopter[row, col] > smallest_blocking:
            n_visible += 1

print('Part One:', n_visible)

highest_scenic_score = 0

for row in range(1, grid_size-1):
    for col in range(1, grid_size-1):
        tree = quadcopter[row, col]

        r = row - 1
        viewing_distance = 0
        while r >= 0:
            if tree <= quadcopter[r, col]:
                viewing_distance += 1
                break
            else:
                viewing_distance += 1
                r -= 1

        scenic_score = viewing_distance

        r = row + 1
        viewing_distance = 0
        while r < grid_size:
            if tree <= quadcopter[r, col]:
                viewing_distance += 1
                break
            else:
                viewing_distance += 1
                r += 1

        scenic_score *= viewing_distance

        c = col - 1
        viewing_distance = 0
        while c >= 0:
            if tree <= quadcopter[row, c]:
                viewing_distance += 1
                break
            else:
                viewing_distance += 1
                c -= 1

        scenic_score *= viewing_distance

        c = col + 1
        viewing_distance = 0
        while c < grid_size:
            if tree <= quadcopter[row, c]:
                viewing_distance += 1
                break
            else:
                viewing_distance += 1
                c += 1

        scenic_score *= viewing_distance

        highest_scenic_score = max(highest_scenic_score, scenic_score)


print('Part Two:', highest_scenic_score)
