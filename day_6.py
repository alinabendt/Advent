import numpy as np

with open('/mnt/c/Users/Uni/Documents/GitHub/Advent/input_day6.txt', 'r') as file:
    signal = file.readlines()
    signal = signal[0].split()
    signal = list(signal[0])
    for c in range(14, len(signal)):
        # check if signal[c-3:c] has 4 unique characters or part 2 14 unique characters
        if len(np.unique(signal[c-14:c])) == 14:
            print(c)
            break
