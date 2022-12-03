with open('../data/puzzle_input_day_03.txt') as f:
    lines = f.read().splitlines()

def return_common_item(rucksack):
    split_index = int(len(rucksack)/2)
    common_item = set(rucksack[:split_index]) & set(rucksack[split_index:])
    return common_item.pop()

def convert_item_to_priority(item):
    delta_lowercase = ord('a') - 1
    delta_uppercase = ord('A') - 27

    if item.islower():
        return ord(item) - delta_lowercase
    else:
        return ord(item) - delta_uppercase


sum_of_priorities = 0
for line in lines:
    common_item = return_common_item(line)
    sum_of_priorities += convert_item_to_priority(common_item)

print('Part One:', sum_of_priorities)

sum_of_priorities = 0
for i in range(0, len(lines), 3):
    common_item = set(lines[i]) & set(lines[i+1]) & set(lines[i+2])
    sum_of_priorities += convert_item_to_priority(common_item.pop())

print('Part Two:', sum_of_priorities)
