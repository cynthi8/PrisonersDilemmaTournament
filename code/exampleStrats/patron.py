# Patron will always defect if they detect a thrower, otherwise they will tit-for-tat
# Memory state represents thower detected (True) or not detected (False)
import numpy as np
secret_message = [0, 0, 1, 1]


def strategy(history, memory):
    if history.shape[1] < len(secret_message):
        return secret_message[history.shape[1]], None
    elif history.shape[1] == len(secret_message):
        if np.array_equal(history[1], secret_message):
            return 0, True
        else:
            return tft_strategy(history), False
    else:
        if memory:
            return 0, True
        else:
            return tft_strategy(history), False


def tft_strategy(history):
    '''
    Copy of default tit-for-tat strategy
    '''
    choice = 1
    # Choose to defect if and only if the opponent just defected.
    if history.shape[1] >= 1 and history[1, -1] == 0:
        choice = 0
    return choice
