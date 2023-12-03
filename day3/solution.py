import sys

rows = []
for line in sys.stdin:
    row = []
    for ch in line.strip():
        row.append(ch)
    rows.append(row)


def symbol_is_neighbor(i, j_start, j_end, rows):
    for j in range(j_start, j_end + 1):
        for del_i in range(i-1, i+2):
            for del_j in range(j-1, j+2):
                if del_i == i and del_j == j:
                    continue
                if del_i < 0 or del_i == len(rows) or del_j < 0 or del_j == len(row):
                    continue
                neighbor_value = rows[del_i][del_j]
                if not neighbor_value.isdigit() and neighbor_value != '.':
                    return True
    return False 
             
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
                if symbol_is_neighbor(i, num_start, j - 1,  rows):
                    total += int(num)
                num = ""
                num_start = None

print(total)
                

        
