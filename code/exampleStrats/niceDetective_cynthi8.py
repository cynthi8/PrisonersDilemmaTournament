# Nice Detective!
# Don't defect first, but try to figure out oppenent if they have defected


def strategy(history, memory):
    """
    :history: 2d numpy array of our and opponent past moves
    :memory: dict
    """
    num_rounds = history.shape[1]
    max_defection_threshold = .5

    if num_rounds == 0:
        # First Round
        choice = 1
        memory = {}
        memory['opponent_defections'] = 0
        memory['opponent_retaliations'] = 0
        memory['my_defections'] = 0
        memory['my_retaliations'] = 0
        memory['defected_unpunished'] = 0

    else:
        # Defection Counts
        opponent_defected = False
        my_defected = False
        if history[1, -1] == 0:
            memory['opponent_defections'] += 1
            opponent_defected = True
        if history[0, -1] == 0:
            memory['my_defections'] += 1
            my_defected = True

        if num_rounds == 1:
            # Second Round (defect if my oppenent started with defect)
            choice = 1
            if history[1, -1] == 0:
                choice = 0
        else:
            # Retaliation Counts
            opponent_retaliated = False
            if history[0, -2] == 0 and history[1, -1] == 0:
                memory['opponent_retaliations'] += 1
                opponent_retaliated = True
            if history[0, -1] == 0 and history[1, -2] == 0:
                memory['my_retaliations'] += 1

            # Did they not punish me for a defection?
            if my_defected and not opponent_retaliated:
                memory['defected_unpunished'] += 1

            # Default Cooperatate
            choice = 1

            # Bounded Patient Tit for Tat
            if opponent_defected:
                choice = 0
                if opponent_retaliated:
                    choice = 1
                    if memory['opponent_defections'] / num_rounds > max_defection_threshold:
                        choice = 0

            # They must be random or preprogrammed -> defect
            if memory['defected_unpunished'] >= 2:
                choice = 0

    return choice, memory
