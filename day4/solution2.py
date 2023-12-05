import sys
import re
from collections import defaultdict

total = 0

card_number_count = defaultdict(lambda: 1)

for line in sys.stdin:
    card_start_match = re.match(r'Card\s+(\d+): ', line)
    card_number = int(card_start_match.group(1))
    rest_of_line = line[len(card_start_match.group(0)):].strip()
    parts = rest_of_line.split("|")
    winning_numbers = parts[0].strip().split()
    my_numbers = parts[1].strip().split()
    winning_numbers_set = set([int(winning_number) for winning_number in winning_numbers])
    card_number_copy = card_number + 1
    for my_number in my_numbers:
        if int(my_number) in winning_numbers_set:
            card_number_count[card_number_copy] += card_number_count[card_number] 
            card_number_copy += 1

total_scorecards = 0
for i in range(1, card_number + 1):
    total_scorecards += card_number_count[i]

print(total_scorecards)
