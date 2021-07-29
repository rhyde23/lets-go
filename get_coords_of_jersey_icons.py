from file_path_converter import convert_path

pi = True

def load_coords_text_file() :
	coords_file_path = 'C:\\Users\\rhyde23\\Desktop\\Project\\coords.txt'
	if pi :
		coords_file_path = convert_path(coords_file_path)
	with open(coords_file_path, 'r') as filename:
		return filename.readlines()

def split_array_by_formation(lines) :
	lines = [line[:-1] for line in lines]
	coords_split_up = []
	current_array = []
	for line in lines :
		if line == '' :
			coords_split_up.append(current_array)
			current_array = []
		else :
			current_array.append(line)
	return coords_split_up

def get_coords_dictionary(split_up_arrays) :
	final_dict = {}
	split_up_arrays = split_up_arrays[:-1]
	for array in split_up_arrays :
		key_name = array[0]
		splitted_by_spaces = key_name.split(' ')
		formation_name = splitted_by_spaces[0]
		specification = ' '.join(splitted_by_spaces[1:])
		key_name = '-'.join(list(formation_name))+' ('+specification+')'
		position_coords_dict = {}
		for line in array[1:] :
			pos, coordinates = line.split('-')
			pos, coordinates = pos[:-1], coordinates[1:].replace(' ', '')
			x, y = coordinates.split(',')
			x, y = int(x[1:]), int(y[:-1])
			position_coords_dict[pos] = (x, y)
		final_dict[key_name] = position_coords_dict
	return final_dict
	
lines = load_coords_text_file()
split_up_arrays = split_array_by_formation(lines)

print(get_coords_dictionary(split_up_arrays))
