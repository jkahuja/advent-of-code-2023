import sys
import re

total = 0

for line in sys.stdin:
    card_start_match = re.match(r'Card\s+(\d+): ', line)
    rest_of_line = line[len(card_start_match.group(0)):].strip()
    parts = rest_of_line.split("|")
    winning_numbers = parts[0].strip().split()
    my_numbers = parts[1].strip().split()
    winning_numbers_set = set([int(winning_number) for winning_number in winning_numbers])
    current_point_value = None
    for my_number in my_numbers:
        if int(my_number) in winning_numbers_set:
            if not current_point_value:
                current_point_value = 1
            else:
                current_point_value *= 2
    total += current_point_value or 0

print(total)
