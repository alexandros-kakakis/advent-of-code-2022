import functools

with open('../data/puzzle_input_day_13.txt') as f:
    lines = f.read().split('\n\n')

lines = [(eval(i.splitlines()[0]), eval(i.splitlines()[1])) for i in lines]


def compare_lists(left, right):

    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        elif left == right:
            return 0
        else:
            return -1

    if isinstance(left, list) and isinstance(right, list):
        for i in range(min(len(left), len(right))):
            result = compare_lists(left[i], right[i])
            if (result == 1) | (str(result) == 'True'):
                return True
            elif (result == -1) | (str(result) == 'False'):
                return False
            else:
                continue

    if isinstance(left, list) and not isinstance(right, list):
        return compare_lists(left, [right])

    if not isinstance(left, list) and isinstance(right, list):
        return compare_lists([left], right)

    if len(left) < len(right):
        return True
    elif len(left) == len(right):
        return 0
    else:
        return False


total = 0
for pair, line in enumerate(lines, start=1):
    left, right = line
    if compare_lists(left, right):
        total += pair

print('Part One:', total)


def compare_lists_sort(a, b):
    if compare_lists(a, b):
        return 1
    else:
        return -1


with open('../data/puzzle_input_day_13.txt') as f:
    lines = f.read().splitlines()

lines = [eval(i) for i in lines if i != '']
lines.append([[2]])
lines.append([[6]])

sorted_lines = sorted(lines, key=functools.cmp_to_key(compare_lists_sort), reverse=True)
result = [i + 1 for (i, line) in enumerate(sorted_lines) if ((line == [[2]]) | (line == [[6]]))]
print('Part Two:', result[0]*result[1])
