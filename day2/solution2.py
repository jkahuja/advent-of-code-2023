import sys
import re
import math

color_pattern = r'(\d+) ([a-zA-Z]+)'

sum_of_powers = 0


for line in sys.stdin:
    game_index_match = re.match(r'Game (\d+):', line)
    game_index = int(game_index_match.group(1))
    game_line = line[len(game_index_match.group(0)):].strip()
    games = game_line.split(';')
    color_max = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    
    for game in games:
        matches = re.finditer(color_pattern, game)
        for match in matches:
            count = int(match.group(1))
            color = match.group(2)
            color_max[color] = max(color_max[color], count)
        
    power = math.prod(color_max.values())
    sum_of_powers += power

    
print(sum_of_powers)
