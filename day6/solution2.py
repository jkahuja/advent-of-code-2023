import sys

line1 = sys.stdin.readline().strip().split()
time = int(''.join([time for time in line1[1:]]))

line2 = sys.stdin.readline().strip().split()
distance = int(''.join([distance for distance in line2[1:]]))


for button_time in range(1, time):
    distance_moved = button_time * (time - button_time)
    if distance_moved > distance:
        lowest_winning_value = button_time
        break

for button_time in range(time - 1, 1, -1):
    distance_moved = button_time * (time - button_time)
    if distance_moved > distance:
        highest_winning_value = button_time
        break



print(highest_winning_value - lowest_winning_value + 1)
        
    

