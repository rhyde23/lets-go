def convert_path(path) :
    path = path.replace('C:\\Users\\rhyde23\\', '/home/pi/').replace('\\', '/').replace('SoccerManager', 'Project')
    return path
