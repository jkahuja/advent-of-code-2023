import sys

line1 = sys.stdin.readline().strip().split()
times = [int(time) for time in line1[1:]]

line2 = sys.stdin.readline().strip().split()
distances = [int(distance) for distance in line2[1:]]

total_product = 1

for i in range(0, len(times)):
    race_time = times[i]
    total_ways_to_win = 0
    for button_time in range(1, race_time):
        distance_moved = button_time * (race_time - button_time)
        if distance_moved > distances[i]:
            total_ways_to_win += 1
    total_product *= total_ways_to_win

print(total_product)
        
    
