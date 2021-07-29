import pickle
from file_path_converter import convert_path
#make 10 save files

pi = True


"""teams_in_league = [
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
]"""
teams_in_league = [
    'Arsenal',
    'Aston Villa'
]


dictionary = {
    'TeamName':'',
    'ManagerName':'',
    'CurrentLineup':[],
    'CurrentFormation':'',
    'CurrentBudget':0,
    'CurrentTeamOverall':0,
    'DaysAdvanced':0,
    'CurrentDate':'June 1 2020',
    'CurrentEmails':[],
    'UnreadEmails':0,
    'CurrentStandings':{},
    'CurrentStandingsInOrder':[],
    'TopScorers':{},
    'TopScorersInOrder':[],
    'TopAssistors':{},
    'TopAssistorsInOrder':[],
    'Arsenal_Players':{},
    'Arsenal_Formation':'4-2-3-1 (Wide)',
    'Arsenal_Lineup':['Bernd Leno', 'Hector Bellerin', 'David Luiz', 'Gabriel', 'Kieran Tierney', 'Thomas Partey', 'Granit Xhaka', 'Bukayo Saka', 'Gabriel Martinelli', 'Martin Odegaard', 'Alexandre Lacazette'],
    'Aston Villa_Players':{},
    'Aston Villa_Formation':'4-2-3-1 (Wide)',
    'Aston Villa_Lineup':['Emiliano Martinez', 'Matty Cash', 'Ezri Konsa', 'Tyrone Mings', 'Matt Targett', 'Douglas Luiz', 'John McGinn', 'Bertrand Traore', 'Anwar El Ghazi', 'Jack Grealish', 'Ollie Watkins'],
}

for team in teams_in_league :
    if pi :
        team_path = convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\'+team+'.dat')
    else :
        team_path = 'C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\'+team+'.dat'
    key = team+'_Players'
    dictionary[key] = pickle.load(open(convert_path(team_path), 'rb'))

basic_info_dictionary = {
    'SaveName':'EMPTY SAVE'
}

for i in range(1, 11) :
    print(i)    
    file_path = ''.join(['C:\\Users\\rhyde23\\Desktop\\SoccerManager\\Saves', '\\File', str(i), '.dat'])
    if pi :
        file_path = convert_path(file_path)
    output_file = open(file_path, 'wb')
    pickle.dump(dictionary, output_file)
    file_path = ''.join(['C:\\Users\\rhyde23\\Desktop\\SoccerManager\\Saves', '\\File', str(i), 'BasicInfo.dat'])
    if pi :
        file_path = convert_path(file_path)
    output_file = open(file_path, 'wb')
    pickle.dump(basic_info_dictionary, output_file)


file_path = ''.join(['C:\\Users\\rhyde23\\Desktop\\SoccerManager\\Saves', '\\ThrowawayFile.dat'])
if pi :
    file_path = convert_path(file_path)
output_file = open(file_path, 'wb')
pickle.dump(dictionary, output_file)

