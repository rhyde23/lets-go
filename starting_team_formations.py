"""string = 
formations = {
    '4-2-3-1 (Wide)':['GK', 'RB', 'RCB', 'LCB', 'LB', 'RDM', 'LDM', 'RM', 'LM', 'CAM', 'ST'],
    '5-3-2 (Attacking)':['GK', 'RWB', 'RCB', 'CB', 'LCB', 'LWB', 'RCM', 'LCM', 'CAM', 'RS', 'LS'],
    '4-4-2 (Flat)':['GK', 'RB', 'RCB', 'LCB', 'LB', 'RM', 'RCM', 'LCM', 'LM', 'RS', 'LS'],
    '5-2-3 (Flat)':['GK', 'RWB', 'RCB', 'CB', 'LCB', 'LWB', 'RCM', 'LCM', 'RW', 'ST', 'LW'],
    '4-3-3 (Defensive)':['GK', 'RB', 'RCB', 'LCB', 'LB', 'CDM', 'RCM', 'LCM', 'RW', 'ST', 'LW'],
    '4-5-1 (Defensive)':['GK', 'RB', 'RCB', 'LCB', 'LB', 'CDM', 'RM', 'RCM', 'LCM', 'LM', 'ST'],
    '4-3-3 (False 9)':['GK', 'RB', 'RCB', 'LCB', 'LB', 'CDM', 'RCM', 'LCM', 'CF', 'RW', 'LW'],
    '5-3-2 (Flat)':['GK', 'RWB', 'RCB', 'CB', 'LCB', 'LWB', 'RCM', 'CM', 'LCM', 'RS', 'LS'],
    '4-3-3 (Flat)':['GK', 'RB', 'RCB', 'LCB', 'LB', 'RCM', 'CM', 'LCM', 'RW', 'ST', 'LW'],
    '4-3-3 (Attacking)':['GK', 'RB', 'RCB', 'LCB', 'LB', 'RCM', 'LCM', 'CAM', 'RW', 'ST', 'LW'],
    '4-2-3-1 (Narrow)':['GK', 'RB', 'RCB', 'LCB', 'LB', 'RDM', 'LDM', 'RAM', 'CAM', 'LAM', 'ST'],
    '4-1-2-1-2 (Narrow)':['GK', 'RB', 'RCB', 'LCB', 'LB', 'CDM', 'LCM', 'RCM', 'CAM', 'LS', 'RS'],
}


splitted = string.split('\n')[2:][:-2]
for s in splitted :
    formation, order = s.split(':')
    print('if formation == '+formation[3:]+' :')
    print('    return '+order[:-1])
quit()
"""


def get_positions_from_formation(formation) :
    if formation ==  '4-2-3-1 (Wide)' :
        return ['GK', 'RB', 'RCB', 'LCB', 'LB', 'RDM', 'LDM', 'RM', 'LM', 'CAM', 'ST']
    if formation ==  '5-3-2 (Attacking)' :
        return ['GK', 'RWB', 'RCB', 'CB', 'LCB', 'LWB', 'RCM', 'LCM', 'CAM', 'RS', 'LS']
    if formation ==  '4-4-2 (Flat)' :
        return ['GK', 'RB', 'RCB', 'LCB', 'LB', 'RM', 'RCM', 'LCM', 'LM', 'RS', 'LS']
    if formation ==  '5-2-3 (Flat)' :
        return ['GK', 'RWB', 'RCB', 'CB', 'LCB', 'LWB', 'RCM', 'LCM', 'RW', 'ST', 'LW']
    if formation ==  '4-3-3 (Defensive)' :
        return ['GK', 'RB', 'RCB', 'LCB', 'LB', 'CDM', 'RCM', 'LCM', 'RW', 'ST', 'LW']
    if formation ==  '4-5-1 (Defensive)' :
        return ['GK', 'RB', 'RCB', 'LCB', 'LB', 'CDM', 'RM', 'RCM', 'LCM', 'LM', 'ST']
    if formation ==  '4-3-3 (False 9)' :
        return ['GK', 'RB', 'RCB', 'LCB', 'LB', 'CDM', 'RCM', 'LCM', 'CF', 'RW', 'LW']
    if formation ==  '5-3-2 (Flat)' :
        return ['GK', 'RWB', 'RCB', 'CB', 'LCB', 'LWB', 'RCM', 'CM', 'LCM', 'RS', 'LS']
    if formation ==  '4-3-3 (Flat)' :
        return ['GK', 'RB', 'RCB', 'LCB', 'LB', 'RCM', 'CM', 'LCM', 'RW', 'ST', 'LW']
    if formation ==  '4-3-3 (Attacking)' :
        return ['GK', 'RB', 'RCB', 'LCB', 'LB', 'RCM', 'LCM', 'CAM', 'RW', 'ST', 'LW']
    if formation ==  '4-2-3-1 (Narrow)' :
        return ['GK', 'RB', 'RCB', 'LCB', 'LB', 'RDM', 'LDM', 'RAM', 'CAM', 'LAM', 'ST']
    if formation ==  '4-1-2-1-2 (Narrow)' :
        return ['GK', 'RB', 'RCB', 'LCB', 'LB', 'CDM', 'LCM', 'RCM', 'CAM', 'LS', 'RS']

