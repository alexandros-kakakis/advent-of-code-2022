import re

with open('../data/puzzle_input_day_05.txt') as f:
    lines = f.read().splitlines()

split_index = [i for i, x in enumerate(lines) if x == ''][0]
n_stacks = int(lines[split_index - 1].split()[-1])
starting_stacks = lines[:split_index - 1][::-1]
procedure_list = [[int(j) for j in i] for i in [re.findall(r'(\d+)', p) for p in lines[split_index + 1:]]]


def create_stack_dict(starting_stacks, n_stacks):
    stacks = {k: [] for k in range(n_stacks)}

    for stack in starting_stacks:
        for stack_index, crate_locator in enumerate(range(1, (4 * n_stacks - 1), 4)):
            crate = stack[crate_locator]
            if crate != ' ':
                stacks[stack_index].append(crate)

    return stacks


def rearrange_crates_part_one(stacks, procedure_list):
    for procedure in procedure_list:
        n_crates, from_stack, to_stack = procedure

        for _ in range(n_crates):
            crate = stacks[from_stack - 1].pop(-1)
            stacks[to_stack - 1].append(crate)

    return stacks


def rearrange_crates_part_two(stacks, procedure_list):
    for procedure in procedure_list:
        n_crates, from_stack, to_stack = procedure

        crates = stacks[from_stack - 1][-(n_crates):]
        stacks[to_stack - 1] += crates
        stacks[from_stack - 1] = stacks[from_stack - 1][:-n_crates]

    return stacks


def return_top_crates(stacks):
    return ''.join([i[-1] for i in stacks.values()])


stacks = create_stack_dict(starting_stacks, n_stacks)
result = rearrange_crates_part_one(stacks, procedure_list)
print('Part One:', return_top_crates(result))

stacks = create_stack_dict(starting_stacks, n_stacks)
result = rearrange_crates_part_two(stacks, procedure_list)
print('Part Two:', return_top_crates(result))

