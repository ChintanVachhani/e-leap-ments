# generates a random table of data
# call this once at the beginning of the game and save it as a variable which can be accessed by the function calculate_score()

import numpy as np


def generate_random_table():
    a = np.random.normal(loc=1.0, scale=.8, size=(4, 4))

    # turn negatives into positives and make overpowered numbers more rare
    for i in np.arange(4):
        for j in np.arange(4):
            if a[i, j] < 0:
                a[i, j] *= -1.00
            if a[i, j] > 1.5:
                a[i, j] -= .500
    # print(a)
    return a

# generate_random_table()
