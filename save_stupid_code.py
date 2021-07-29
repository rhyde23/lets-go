
"""
def rearrange_lineup_formation_change(new_formation, new_positions) :
    best_options_each_pos = {}
    final_new, used = {}, []
    while True :
        f = False
        for new_position in new_positions :
            converted_pos = convert_outside_position_to_center(new_position)
            if converted_pos in ['RB', 'RWB'] :
                converted_pos_array = ['RB', 'RWB']
            elif converted_pos in ['LB', 'LWB'] :
                converted_pos_array = ['LB', 'LWB']
            else :
                converted_pos_array = [converted_pos]
            best_options = [option for option in get_best_players_in_given_position(team, converted_pos) if option in current_data['CurrentLineup'] and not option in used]
            if current_data[team+'_Players'][best_options[0]]['Position'] in converted_pos_array :
                best_options_each_pos = {}
                final_new[new_position] = best_options[0]
                used.append(best_options[0])
                new_positions.remove(new_position)
                f = True
                break
            else :
                best_options_each_pos[new_position] = best_options
        if not f :
            break
    
    print(len(final_new))
    if len(final_new) != 11 :
        left_positions_order = list(best_options_each_pos.keys())
        left_players = best_options_each_pos[left_positions_order[0]]
        if len(final_new) == 10 :
            final_new[left_positions_order[0]] = left_players[0]
        else :
            for permu_standards in [[1.0, 1.1], [1.0, 1.1, 1.2], [1.0, 1.1, 1.2, 1.3], [1.0, 1.1, 1.2, 1.3, 1.4], [1.0, 1.1, 1.2, 1.3, 1.4, 1.5]] :
                current_lineup_position_ratings = {n:{pos:current_data[team+'_Players'][n]['Positions'][convert_outside_position_to_center(pos)] for pos in left_positions_order} for n in left_players}
                current_lineup_position_percentages = {n:{pos:round((int(current_data[team+'_Players'][n]['Rating'])/current_data[team+'_Players'][n]['Positions'][convert_outside_position_to_center(pos)]), 1) for pos in left_positions_order} for n in left_players}
                number_in_combo = len(left_players)
                permu_arrays = [[] for xyz in range(number_in_combo)]
                for cipp in current_lineup_position_percentages :
                    for cipp_position in current_lineup_position_percentages[cipp] :
                        if current_lineup_position_percentages[cipp][cipp_position] in permu_standards :
                            permu_arrays[left_positions_order.index(cipp_position)].append(cipp)
                    
                if not [] in permu_arrays :
                    failed = False
                    for le in left_players :
                        alright = False
                        for p_a in permu_arrays :
                            if le in p_a :
                                alright = True
                                break
                        if not alright :
                            failed = True
                    if failed :
                        continue
                else :
                    continue
                    
                highest_rating = 0
                all_same_attempts = []
                amount_of_permutations = 0
                combos = [[element] for element in permu_arrays[0]]
                current_permu_index = 1
                while combos != [] :
                    new_combos = []
                    for combo in combos :
                        for element in [element for element in permu_arrays[current_permu_index] if not element in combo] :
                            new_addition = combo+[element]
                            if len(new_addition) == number_in_combo :
                                attempt = determine_rating_of_combo(new_addition, left_positions_order, current_lineup_position_ratings, number_in_combo)
                                if attempt > highest_rating :
                                    highest_rating = attempt
                                    all_same_attempts = [new_addition]
                                if attempt == highest_rating :
                                    all_same_attempts.append(new_addition)
                                amount_of_permutations += 1
                            else :
                                new_combos.append(new_addition)
                    combos = new_combos
                    current_permu_index += 1
                print()
                print('Performance:', amount_of_permutations)
                best, best_r = (), 0
                for a in all_same_attempts :
                    points = get_correct_general_placements(left_positions_order, a)
                    if points >= best_r :
                        best, best_r = a, points
                try :
                    for i in range(number_in_combo)  :
                        final_new[left_positions_order[i]] = best[i]
                    break
                except :
                    pass
    return [final_new[n_pos] for n_pos in get_positions_from_formation(new_formation)]
"""
