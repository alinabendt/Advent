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


with open('/home/alina/Advent/input_day10.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        line = line.split(' ')
        strength, cycle, xs = execute(strength, cycle, xs, line)
print(strength)
s = [strength.get(key) for key in strength.keys()]
print('sum of signal strengths: ', np.sum(s))

# part 2
def sprite(x):
    pos = [x-1, x, x+1]
    return pos


def draw(x, c_line):
    sprite_pos = sprite(x)
    if len(c_line) in sprite_pos:
        c_line = c_line+"#"
    else:
        c_line = c_line+"."
    return c_line


def execute2(strength, c, x, com, c_line, display):
    if com[0] == 'noop':
        strength = check_cycle(strength, c, x)
        c_line, display = check_line(c_line, display)
        c_line= draw(x, c_line)
        c += 1
    else:
        for _ in range(2):
            strength = check_cycle(strength, c, x)
            c_line, display = check_line(c_line, display)
            c_line = draw(x, c_line)
            c += 1
        x += [int(d) for d in re.findall(r'-?\d+', com[1])][0]
    return c_line, strength, c, x, display


def check_line(c_line, display):
    if len(c_line) == 40:
        display.append(c_line)
        c_line = str()
    return c_line, display


with open('/home/alina/Advent/input_day10.txt', 'r') as file:
    display = []
    c_line = str()
    xs = 1
    for line in file:
        line = line.strip('\n')
        line = line.split(' ')
        c_line, strength, cycle, xs, display = execute2(strength, cycle, xs, line, c_line, display)
        c_line, display = check_line(c_line, display)
for i in range(np.size(display)):
    print(display[i])
