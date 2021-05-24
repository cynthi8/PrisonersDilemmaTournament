# Thrower will always coorperate if they detect their patron, otherwise they will always defect
# Memory state represents patron detected (True) or not detected (False)
import numpy as np
secret_message = [0, 0, 1, 1]


def strategy(history, memory):
    if history.shape[1] < len(secret_message):
        return secret_message[history.shape[1]], None
    elif history.shape[1] == len(secret_message):
        if np.array_equal(history[1], secret_message):
            return 1, True
        else:
            return 0, False
    else:
        if memory:
            return 1, True
        else:
            return 0, False
