#Get All possible data strings

import pickle
from file_path_converter import convert_path

pi = False

teams_in_league = [
    'Arsenal',
    'Aston Villa',
    'Brighton & Hove Albion',
    'Burnley',
    'Chelsea',
    'Crystal Palace',
    'Everton',
    'Fulham',
    'Leeds United',
    'Leicester City',
    'Liverpool',
    'Manchester City',
    'Manchester United',
    'Newcastle United',
    'Sheffield United',
    'Southampton',
    'Tottenham Hotspur',
    'West Bromwich Albion',
    'West Ham United',
    'Wolverhampton Wanderers'
]

data_keys = [
    'Rating',
    'Position',
    'Age',
    'Nation',
    'Height',
    'Weight',
    'Freshness',
    'Goals',
    'Assists',
]

def main() :
    data_collected = {data_key:[] for data_key in data_keys}
    for team_gathering in teams_in_league :
        team_path = 'C:\\Users\\astoa23\\Desktop\\Project\\Team Database\\'+team_gathering+'.dat'
        if pi :
            team_path = convert_path(team_path)
        data_dictionary = pickle.load(open(team_path, 'rb'))
        for p_name in data_dictionary :
            for k in data_keys :
                value = data_dictionary[p_name][k]
                if not value in data_collected[k] :
                    data_collected[k].append(value)
    for g_or_a in range(1, 51) :
        data_collected['Goals'].append(g_or_a)
        data_collected['Assists'].append(g_or_a)
    data_collected = {key:sorted(data_collected[key]) for key in data_collected}
    return data_collected

result = main()
print(result)
