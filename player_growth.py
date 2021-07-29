import time

#Factors
#How high the rating is
#How young the player is

"""current_decrease = 0.01
change_count = 0
current_factor = 1.5

rating_factors = {}

for i in range(50, 100) :
    rating_factors[i] = current_factor 
    change_count += 1
    if change_count == 10 :
        current_decrease += 0.01
        current_decrease = round(current_decrease, 2)
        change_count = 0
    current_factor -= current_decrease
    current_factor = round(current_factor, 2)
    print(current_decrease)
    
print(rating_factors)"""

rating_factors = {
    50: 1.5,
    51: 1.49,
    52: 1.48,
    53: 1.47,
    54: 1.46,
    55: 1.45,
    56: 1.44,
    57: 1.43,
    58: 1.42,
    59: 1.41,
    60: 1.39,
    61: 1.37,
    62: 1.35,
    63: 1.33,
    64: 1.31,
    65: 1.29,
    66: 1.27,
    67: 1.25,
    68: 1.23,
    69: 1.21,
    70: 1.18,
    71: 1.15,
    72: 1.12,
    73: 1.09,
    74: 1.06,
    75: 1.03,
    76: 1.0,
    77: 0.97,
    78: 0.94,
    79: 0.91,
    80: 0.87,
    81: 0.83,
    82: 0.79,
    83: 0.75,
    84: 0.71,
    85: 0.67,
    86: 0.63,
    87: 0.59,
    88: 0.55,
    89: 0.51,
    90: 0.46,
    91: 0.41,
    92: 0.36,
    93: 0.31,
    94: 0.26,
    95: 0.21,
    96: 0.16,
    97: 0.11,
    98: 0.06,
    99: 0.01,
}

age_factors = {
    16:5,
    17:4.7,
    18:4.4,
    19:4.1,
    20:3.8,
    21:3.5,
    22:3.2,
    23:2.9,
    24:2.6,
    25:2.3,
    26:2,
    27:1.7,
    28:1.4,
    29:1.1,
    30:0.8,
    31:0.5,
    32:0.2,
}


def calculate_player_growth(rating, age, freshness) :
    return rating+(round(round(round(rating_factors[rating]*age_factors[age], 2)*freshness, 2)*0.15, 2))


#print(calculate_player_growth(70, 19, 0.5))
    