
def shape_point(shape: str) -> int:
    return ['X', 'Y', 'Z'].index(shape) + 1

def game_point(opp_shape: str, player_shape: str) -> int:
    '''
    Point won on a game
    '''
    match opp_shape:
        case "A":
            if player_shape == "X":
                return 3
            if player_shape == "Y":
                return 6
            return 0
        case "B":
            if player_shape == "X":
                return 0
            if player_shape == "Y":
                return 3
            return 6
        case "C":
            if player_shape == "X":
                return 6
            if player_shape == "Y":
                return 0
            return 3

def get_value(opp_shape: str, player_shape: str) -> int:
    match player_shape:
        case "X":
            if opp_shape == "A":
                return 3
            if opp_shape == "B":
                return 1
            if opp_shape == "C":
                return 2
        case "Y":
            if opp_shape == "A":
                return 4
            if opp_shape == "B":
                return 5
            if opp_shape == "C":
                return 6
        case "Z":
            if opp_shape == "A":
                return 8
            if opp_shape == "B":
                return 9
            if opp_shape == "C":
                return 7

with open('data.txt', encoding='utf-8') as f:
    tours = [x.replace('\n', '') for x in f.readlines() if x.replace('\n', '')]
    total = sum([shape_point(tour[-1]) + game_point(tour[0], tour[-1]) for tour in tours])
    total_2 = sum([get_value(tour[0], tour[-1]) for tour in tours])

print(total)
print(total_2)
