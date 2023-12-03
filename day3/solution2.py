import sys
from dataclasses import dataclass
from collections import defaultdict

rows = []
for line in sys.stdin:
    row = []
    for ch in line.strip():
        row.append(ch)
    rows.append(row)

@dataclass(frozen=True)
class Coordinate:
    row: int
    col: int

@dataclass
class GearRatio:
    first_val: int
    second_val: int
    valid: bool


gear_ratio_dict: dict[Coordinate, GearRatio] = defaultdict(lambda: GearRatio(None, None, True))


def update_gear_ratio(i, j_start, j_end, rows, num):
    for j in range(j_start, j_end + 1):
        for del_i in range(i-1, i+2):
            for del_j in range(j-1, j+2):
                if del_i == i and del_j == j:
                    continue
                if del_i < 0 or del_i == len(rows) or del_j < 0 or del_j == len(row):
                    continue
                neighbor_value = rows[del_i][del_j]
                if neighbor_value == '*':
                    coordinate = Coordinate(del_i, del_j)
                    cur_gear_ratio = gear_ratio_dict[coordinate]
                    if cur_gear_ratio.first_val == num or cur_gear_ratio.second_val == num:
                        continue
                    if cur_gear_ratio.first_val and cur_gear_ratio.second_val:
                        cur_gear_ratio.valid = False
                        continue
                    if not cur_gear_ratio.first_val:
                        cur_gear_ratio.first_val = num
                    else:
                        cur_gear_ratio.second_val = num
             
total = 0
for i, row in enumerate(rows):
    num = ""
    num_start = None
    for j, cell in enumerate(row):
        if cell.isdigit():
            num += cell
            if not num_start:
                num_start = j
        if j == len(row) - 1 or not cell.isdigit():
            if num:
                update_gear_ratio(i, num_start, j - 1, rows, int(num))
                num = ""
                num_start = None

total = 0
for coord, ratio in gear_ratio_dict.items():
    if not ratio.first_val or not ratio.second_val or not ratio.valid:
        continue
    total += ratio.first_val * ratio.second_val


print(total)
      

        

