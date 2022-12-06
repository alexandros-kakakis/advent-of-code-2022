with open('../data/puzzle_input_day_06.txt') as f:
    line = f.read()

def find_number_of_parsed_characters(datastream, n_characters):
    for marker in range(0, len(datastream)):
        charset = set( line[marker:marker+n_characters] )
        if len(charset) == n_characters:
            return marker + n_characters
            break


print('Part One:', find_number_of_parsed_characters(line, n_characters=4))
print('Part Two:', find_number_of_parsed_characters(line, n_characters=14))
