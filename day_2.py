import numpy as np

def play(first, second):
    win = 6
    draw = 3
    loss = 0
    rock = 1
    paper = 2
    scissors = 3
    if first == 'A':
        if second == 'X':
            points = rock+draw
        if second == 'Y':
            points = paper+win
        if second == 'Z':
            points = scissors+loss
    if first == 'B':
        if second == 'X':
            points = rock+loss
        if second == 'Y':
            points = paper+draw
        if second == 'Z':
            points = scissors+win
    if first == 'C':
        if second == 'X':
            points = rock+win
        if second == 'Y':
            points = paper+loss
        if second == 'Z':
            points = scissors+draw
    return points


# AX = Rock, BY = Paper, CZ = Scissors
ps = np.array([])
with open('/mnt/c/Users/Uni/Documents/GitHub/Advent/input_day2.txt', 'r') as file:
    for line in file:
        point = play(line[0], line[2])
        ps = np.append(ps, point)
total_points = np.sum(ps)
print(total_points)

# part 2: X=lose, Y=draw, Z=win
def play2(first, outcome):
    win = 6
    draw = 3
    loss = 0
    rock = 1 #A
    paper = 2 #B
    scissors = 3 #C
    if outcome == 'X':
        if first == 'A':
            points = scissors+loss
        if first == 'B':
            points = rock+loss
        if first == 'C':
            points = paper+loss
    if outcome == 'Y':
        if first == 'A':
            points = rock+draw
        if first == 'B':
            points = paper+draw
        if first == 'C':
            points = scissors+draw
    if outcome == 'Z':
        if first == 'A':
            points = paper+win
        if first == 'B':
            points = scissors+win
        if first == 'C':
            points = rock+win
    return points

ps = np.array([])
with open('/mnt/c/Users/Uni/Documents/GitHub/Advent/input_day2.txt', 'r') as file:
    for line in file:
        point = play2(line[0], line[2])
        ps = np.append(ps, point)
total_points = np.sum(ps)
print(total_points)

