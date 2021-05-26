def strategy(history, memory):
    choice = 1
    if not memory:
        # Choose to defect if and only if the opponent just defected.
        if history.shape[1] >= 1 and history[1, -1] == 0:
            memory = True
            choice = 0
        if history.shape[1] == 200:
            memory = True
    else:
        # Backstab mode
        choice = 0
        if history[0, -1] == 0 and history[1, -1] == 1:
            # If they punish us, go back to cooperation
            choice = 1
            memory = False
    
    return choice, memory
