import sys

total = 0

for line in sys.stdin:
    first_num = None
    last_num = None
    for ch in line:
        try:
            int(ch)
            if not first_num:
                first_num = ch
                last_num = ch
            else:
                last_num = ch
        except:
            pass
    total += int(first_num + last_num)

print(total)
    

     
