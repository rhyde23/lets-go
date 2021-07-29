outside_positions = {
    'LCB':'CB',
    'RCB':'CB',
    'RDM':'CDM',
    'LDM':'CDM',
    'RCM':'CM',
    'LCM':'CM',
    'RS':'ST',
    'LS':'ST',
    'LAM':'CAM',
    'RAM':'CAM'
}

def convert_outside_position_to_center(position) :
    if position in outside_positions :
        return outside_positions[position]
    return position