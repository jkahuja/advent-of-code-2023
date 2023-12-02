import sys
import re

color_pattern = r'(\d+) ([a-zA-Z]+)'

color_limits = {
    "red": 12,
    "green": 13,
    "blue": 14
}

total = 0

def check_game_valid(game_colors):
    for color, count in game_colors.items():
        if color not in color_limits:
            return False

        if color_limits[color] < count:
            return False

    return True

for line in sys.stdin:
    game_index_match = re.match(r'Game (\d+):', line)
    game_index = int(game_index_match.group(1))
    game_line = line[len(game_index_match.group(0)):].strip()
    games = game_line.split(';')
    is_game_valid = True

    for game in games:
        game_colors = {}

        matches = re.finditer(color_pattern, game)
        for match in matches:
            count = int(match.group(1))
            color = match.group(2)
            game_colors[color] = count

        is_game_valid = is_game_valid and check_game_valid(game_colors)
        if not is_game_valid:
            break

    if is_game_valid:
        total += game_index
    print(line, is_game_valid, total)

    
print(total)
