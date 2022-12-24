import re
import numpy as np

cycle = 1
xs = 1
strength = {'20': 0, '60': 0, '100': 0, '140': 0, '180': 0, '220': 0}


def check_cycle(strength, cyc, x):
    if str(cyc) in strength.keys():
        strength[str(cyc)] = x*cyc
    return strength


def execute(strength, c, x, com):
    if com[0] == 'noop':
        strength = check_cycle(strength, c, x)
        c += 1
    else:
        for _ in range(2):
            strength = check_cycle(strength, c, x)
            c += 1
        x += [int(d) for d in re.findall(r'-?\d+', com[1])][0]
    return strength, c, x
        

with open('/mnt/c/Users/Uni/Documents/GitHub/Advent/input_day10.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        line = line.split(' ')
        strength, cycle, xs = execute(strength, cycle, xs, line)
print(strength)
s = [strength.get(key) for key in strength.keys()]
print('sum of signal strengths: ', np.sum(s))

# part 2
