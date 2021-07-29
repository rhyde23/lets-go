import pickle
from file_path_converter import convert_path

pi = True

file_path = 'C:\\Users\\rhyde23\\Desktop\\Project\\TransferCombinations.dat'
if pi :
    file_path = convert_path(file_path)
transfer_combinations = pickle.load(open(file_path, 'rb'))

rating_factors = list(reversed(list(range(50, 94))))
age_factors = list(reversed(list(range(16, 40))))
position_factors = [
    'GK', 
    'RWB', 
    'LWB', 
    'LB', 
    'RB', 
    'CB', 
    'CM', 
    'CDM', 
    'CAM',
    'CF', 
    'LM', 
    'LW',
    'RM', 
    'RW',
    'ST'
]

def build_key(position_factor, rating_factor, age_factor) :
    return '|'.join([position_factor, str(rating_factor), str(age_factor)])

default_pos, default_rat, default_ag = 'CM', '75', '25'
#default_key = build_key(default_pos, default_rat, default_age)
#default_cost = transfer_combinations[default_key]

position_numbers = {position_factor:[] for position_factor in position_factors}    
    
for default_rating in rating_factors :
    default_rating = str(default_rating)
    for default_age in age_factors :
        default_age = str(default_age)
        default_key = build_key(default_pos, default_rating, default_age)
        if default_key in transfer_combinations :
            default_cost = transfer_combinations[default_key]
            for position_factor in position_factors :
                try :
                    test_cost = build_key(position_factor, default_rating, default_age)
                    position_numbers[position_factor].append(transfer_combinations[test_cost]/default_cost)
                except :
                    #print(position_factor)
                    pass

position_numbers = {position_number:sum(position_numbers[position_number])/len(position_numbers[position_number]) for position_number in position_numbers}

print(position_numbers)



rating_numbers = {str(rating_factor):[] for rating_factor in rating_factors}    
    
for default_position in position_factors :
    default_position = str(default_position)
    for default_age in age_factors :
        default_age = str(default_age)
        default_key = build_key(default_position, default_rat, default_age)
        if default_key in transfer_combinations :
            default_cost = transfer_combinations[default_key]
            for rating_factor in rating_factors :
                try :
                    test_cost = build_key(default_position, rating_factor, default_age)
                    rating_numbers[str(rating_factor)].append(transfer_combinations[test_cost]/default_cost)
                except :
                    #print(rating_factor, 'REEEEEE')
                    pass

rating_numbers = {rating_number:sum(rating_numbers[rating_number])/len(rating_numbers[rating_number]) for rating_number in rating_numbers}

print(rating_numbers)




age_numbers = {str(age_factor):[] for age_factor in age_factors}    
    
for default_position in position_factors :
    default_position = str(default_position)
    for default_rating in rating_factors :
        default_rating = str(default_rating)
        default_key = build_key(default_position, default_rating, default_ag)
        if default_key in transfer_combinations :
            default_cost = transfer_combinations[default_key]
            for age_factor in age_factors :
                try :
                    test_cost = build_key(default_position, default_rating, age_factor)
                    age_numbers[str(age_factor)].append(transfer_combinations[test_cost]/default_cost)
                except :
                    #print(rating_factor, 'REEEEEE')
                    pass


age_numbers = {age_number:sum(age_numbers[age_number])/len(age_numbers[age_number]) for age_number in age_numbers}

print(age_numbers)

base_position, base_rating, base_age = 'CM', '75', '25'
base_key = build_key(base_position, base_rating, base_age)
base_cost = transfer_combinations[base_key]

#test_position, test_rating, test_age = 'CDM', '84', '35' 

for test_position in position_factors :
    for test_rating in rating_factors :
        test_rating = str(test_rating)
        for test_age in age_factors :
            test_age = str(test_age)
            built_key = build_key(test_position, test_rating, test_age)
            result = int(base_cost*rating_numbers[test_rating]*age_numbers[test_age]*position_numbers[test_position])
            """
            str_result = str(result)
            length_str_result = len(str_result)
            rounding_number = -(length_str_result-2)
            print(length_str_result, rounding_number)
            result = int(round(result, rounding_number))
            """
            #print(built_key, result)
            try :
                #print('TEST AGAINST DATABASE: ', transfer_combinations[built_key])
                pass
            except :
                pass
            #print()
