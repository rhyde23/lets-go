import random
from outside_positions_converter import convert_outside_position_to_center
from starting_team_formations import get_positions_from_formation

tiers = [
    ['ST', 'LW', 'RW', 'CF', 'RF', 'LF'],
    ['CAM', 'RM', 'LM'],
    ['CM', 'CDM'],
    ['RB', 'RWB', 'LB', 'LWB', 'CB'],
    ['GK']
]

chances = [
    70,
    25,
    15,
    10,
    0
]


def get_losing_team_score() :
    losing_randomization = random.randint(1, 100)
    if losing_randomization >= 80 :
        return 2
    return random.randint(0, 1)

def r_goals(positions) :
    random.shuffle(positions)
    while True :
        for position in positions :
            for i, tier in enumerate(tiers) :
                if convert_outside_position_to_center(position) in tier :
                    chance = chances[i]
                    break
            randomized = random.randint(1, 100)
            if randomized <= chance :
                return position

def get_name_based_off_of_position(formation, lineup, position) :
    return lineup[get_positions_from_formation(formation).index(position)]

def randomize_goals(team1, team2, team1_lineup, team2_lineup, team1_name, team2_name, team1_formation, team2_formation, winning_team, difference_in_score) :
    losing_score = get_losing_team_score()
    winning_score = losing_score+difference_in_score
    if team1_name == winning_team or winning_team == 'Draw' :
        winning_lineup = team1_lineup
        losing_lineup = team2_lineup
        winning_dict = team1
        losing_dict = team2
        winning_formation = team1_formation
        losing_formation = team2_formation
    elif team2_name == winning_team :
        winning_lineup = team2_lineup
        losing_lineup = team1_lineup
        winning_dict = team2
        losing_dict = team1
        winning_formation = team2_formation
        losing_formation = team1_formation
    winning_scorers, losing_scorers = [], []
    for i in range(winning_score) :
        winning_scorers.append(r_goals(get_positions_from_formation(winning_formation)))
    for i in range(losing_score) :
        losing_scorers.append(r_goals(get_positions_from_formation(losing_formation)))
    if team1_name == winning_team or winning_team == 'Draw' :
        score = '-'.join([str(winning_score), str(losing_score)])
        team1_scorers = [get_name_based_off_of_position(team1_formation, team1_lineup, position) for position in winning_scorers]
        team2_scorers = [get_name_based_off_of_position(team2_formation, team2_lineup, position) for position in losing_scorers]
    elif team2_name == winning_team :
        score = '-'.join([str(losing_score), str(winning_score)])
        team1_scorers = [get_name_based_off_of_position(team1_formation, team1_lineup, position) for position in losing_scorers]
        team2_scorers = [get_name_based_off_of_position(team2_formation, team2_lineup, position) for position in winning_scorers]
    return score, team1_scorers, team2_scorers
            
