from functools import reduce

class Monkey:

    def __init__(self, items, operation, divisible_test, true_outcome, false_outcome):
        self.items = items
        self.operation = operation
        self.divisible_test = divisible_test
        self.true_outcome = true_outcome
        self.false_outcome = false_outcome

        self.items_inspected = 0

    def inspect_part_one(self):
        self.items_inspected += 1

        item = self.items.pop(0)
        item = self.operation(item)
        item = int(item / 3)

        if (item % self.divisible_test) == 0:
            return item, self.true_outcome
        else:
            return item, self.false_outcome

    def inspect_part_two(self, common_divisor):
        self.items_inspected += 1

        item = self.items.pop(0)
        item = self.operation(item)
        item %= common_divisor

        if (item % self.divisible_test) == 0:
            return item, self.true_outcome
        else:
            return item, self.false_outcome


def get_monkey_list():
    return [
        Monkey(items=[75, 75, 98, 97, 79, 97, 64], operation=lambda x: x * 13, divisible_test=19, true_outcome=2,
               false_outcome=7),
        Monkey(items=[50, 99, 80, 84, 65, 95], operation=lambda x: x + 2, divisible_test=3, true_outcome=4,
               false_outcome=5),
        Monkey(items=[96, 74, 68, 96, 56, 71, 75, 53], operation=lambda x: x + 1, divisible_test=11, true_outcome=7,
               false_outcome=3),
        Monkey(items=[83, 96, 86, 58, 92], operation=lambda x: x + 8, divisible_test=17, true_outcome=6,
               false_outcome=1),
        Monkey(items=[99], operation=lambda x: x * x, divisible_test=5, true_outcome=0, false_outcome=5),
        Monkey(items=[60, 54, 83], operation=lambda x: x + 4, divisible_test=2, true_outcome=2, false_outcome=0),
        Monkey(items=[77, 67], operation=lambda x: x * 17, divisible_test=13, true_outcome=4, false_outcome=1),
        Monkey(items=[95, 65, 58, 76], operation=lambda x: x + 5, divisible_test=7, true_outcome=3, false_outcome=6)
    ]


def calculate_monkey_business(monkey_list):
    return reduce(lambda x, y: x * y, sorted([monkey.items_inspected for monkey in monkey_list], reverse=True)[:2])


monkey_list = get_monkey_list()

for _ in range(20):
    for monkey in monkey_list:
        while monkey.items:
            item, next_monkey = monkey.inspect_part_one()
            monkey_list[next_monkey].items.append(item)

print('Part One:', calculate_monkey_business(monkey_list))

monkey_list = get_monkey_list()
common_divisor = reduce(lambda x, y: x * y, [m.divisible_test for m in monkey_list])

for _ in range(10000):
    for monkey in monkey_list:
        while monkey.items:
            item, next_monkey = monkey.inspect_part_two(common_divisor)
            monkey_list[next_monkey].items.append(item)

print('Part Two:', calculate_monkey_business(monkey_list))
