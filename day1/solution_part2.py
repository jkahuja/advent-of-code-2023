import sys

total = 0

digits = {
    "zero": '0',
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9',
}

for line in sys.stdin:
    first_pos = None
    last_pos = None
    first_num = None
    last_num = None
    for digit_str, digit_ch in digits.items():
        search_terms = [digit_str, digit_ch]
        for term in search_terms:
            first_occurrence = line.find(term)
            last_occurrence = line.rfind(term)
            if first_occurrence != -1 and (first_pos is None or first_occurrence < first_pos): 
                first_num = digit_ch
                first_pos = first_occurrence
            if last_occurrence != -1 and (last_pos is None or last_occurrence > last_pos):
                last_num = digit_ch
                last_pos = last_occurrence

    if not last_num:
        last_num = digit_ch

    print(line.strip(), first_num, last_num)
    total += int(first_num + last_num)

print(total)
