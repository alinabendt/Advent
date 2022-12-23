import numpy as np

grid = np.zeros(10,10)
grid[0,0] = 'H'

def move_head(m, pos, pos_t):
    steps = m[1]
    for s in range(m[1]):
        if m[0] == 'R':
            grid[pos] = 0
            pos[1] = pos[1]+steps
        elif m[0] == 'L':
            grid[pos] = 0
            pos[1] = pos[1]-steps
        elif m[0] == 'U':
            grid[pos] = 0
            pos[0] = pos[0]+steps
        elif m[0] == 'D':
            grid[pos] = 0
            pos[0] = pos[0]-steps
        if pos[0]<0 or pos[1]<0 or pos[0]>np.shape(grid)[0] or pos[1]>np.shape(grid)[1]:
            grid = extend(pos)
        grid[pos] = 'H'
        move_tail(pos, pos_t)
    return pos, pos_t

def move_tail(pos_h, pos_t):
    if pos_h[0]

def extend(position):
    if position[0]<0:
        grid = np.insert(np.zeros((1, np.shape(grid)[1])), 0)
    if position[1]<0:
        grid = np.insert(np.zeros((np.shape(grid)[0], 1)), 0)
    if position[0]>np.shape(grid)[0]:
        grid = np.append(grid, np.zeros((1, np.shape(grid)[1])), axis=0)
    if position[1]>np.shape(grid)[1]:
        grid = np.append(grid, np.zeros((np.shape(grid)[0], 1)), axis=1)
    return grid

with open('/mnt/c/Users/Uni/Documents/GitHub/Advent/input_day9.txt', 'r') as file:
    for line in file:
        command = line.strip()
        command = line.split(' ')
        grid = move(command)
