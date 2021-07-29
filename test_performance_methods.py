import pickle
from file_path_converter import convert_path
from team_rating_calculator import calculate_rating
from match_sim_calculator import  match_sim
from goals_randomizer import randomize_goals

pi = True

save_path = 'C:\\Users\\rhyde23\\Desktop\\Project\\Saves\\File1.dat'

if pi :
    save_path = convert_path(save_path)


save = pickle.load(open(save_path, 'rb'))

def test(expected_arsenal_ovr, expected_aston_villa_ovr) :
    arsenal_formation = save['Arsenal_Formation']
    arsenal_players = save['Arsenal_Players']
    arsenal_lineup = save['Arsenal_Lineup']

    aston_villa_formation = save['Aston Villa_Formation']
    aston_villa_players = save['Aston Villa_Players']
    aston_villa_lineup = save['Aston Villa_Lineup']
    

    #Now we actually start testing the functionality

    
    arsenal_rating = calculate_rating(arsenal_players, arsenal_lineup, arsenal_formation)
    
    print(arsenal_rating, 'arsenal rating')

    if arsenal_rating == expected_arsenal_ovr :
        print('Success')
    print()

    aston_villa_rating = calculate_rating(aston_villa_players, aston_villa_lineup, aston_villa_formation)

    print(aston_villa_rating, 'villa rating')
    
    if aston_villa_rating == expected_aston_villa_ovr :
        print('Success')
    print()
    
    winner, score_difference = match_sim(aston_villa_rating, arsenal_rating, 'Aston Villa', 'Arsenal')

    print(winner, score_difference)

    score, aston_villa_scorers, arsenal_scorers = randomize_goals(aston_villa_players, arsenal_players, aston_villa_lineup, arsenal_lineup, 'Aston Villa', 'Arsenal', aston_villa_formation, arsenal_formation, winner, score_difference)

    print(score, aston_villa_scorers, arsenal_scorers)

test(79, 75)
