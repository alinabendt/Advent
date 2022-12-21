import re
import textwrap
import numpy as np


arr = np.zeros((1,9))
counter = 0
with open('/mnt/c/Users/Uni/Documents/GitHub/Advent/input_day5.txt', 'r') as file:
    for line in file:
        crates = []
        if any(i.isnumeric() for i in line):
            break
        line = line.replace(" ", "_")
        # split line into 9 piles of crates
        places = textwrap.wrap(line, int(len(line)/9))
        # find elements of places that contain a crate and add to crates array
        for p in range(len(places)):
            if any(i.isupper() for i in places[p]):
                crates = np.append(crates, places[p].replace("_", ""))
            else:
                crates = np.append(crates, 0)
        arr = np.append(arr, [crates], axis=0)
        counter += 1
arr = np.delete(arr, 0, 0)
arr = np.hsplit(arr, 9)
for i in range(np.shape(arr)[0]):
    arr[i] = np.ndarray.flatten(arr[i])
print(arr)

# move crates
with open('/mnt/c/Users/Uni/Documents/GitHub/Advent/input_day5.txt', 'r') as file:
    moves = file.readlines()[counter+2:]
    for m in range(len(moves)):
        moves[m] = moves[m].strip('\n')
        moves[m] = [int(s) for s in re.findall(r'\d+', moves[m])]

# perform moves
# first number is number of crates, second is from which stack, third is to which stack
def do_move(move, stack):
    for _ in range(move[0]):  # do move n times for n number of crates
        # move top most crate from stack move[1] to move[2]
        # check if top is 0, if yes move down further
        i = 0
        j = 0
        while stack[move[1]-1][i] == '0' or stack[move[1]-1][i] == '0.0':
            i += 1
        if stack[move[2]-1][np.size(stack[move[2]-1])-1] == '0' or stack[move[2]-1][np.size(stack[move[2]-1])-1] == '0.0':
            j = np.size(stack[move[2]-1])
        else:
            while stack[move[2]-1][j] == '0' or stack[move[2]-1][j] == '0.0':
                j += 1
        if j == 0:
            stack[move[2]-1] = np.insert(stack[move[2]-1], 0, stack[move[1]-1][i])
        else:
            stack[move[2]-1][j-1] = stack[move[1]-1][i]
        stack[move[1]-1][i] = '0'
    return

# part 2: move crates in batches
def do_move2(move, stack):
    # move top most crate from stack move[1] to move[2]
    # check if top is 0, if yes move down further
    i = 0
    j = 0
    while stack[move[1]-1][i] == '0' or stack[move[1]-1][i] == '0.0':
        i += 1
    if stack[move[2]-1][np.size(stack[move[2]-1])-1] == '0' or stack[move[2]-1][np.size(stack[move[2]-1])-1] == '0.0':
        j = np.size(stack[move[2]-1])
    else:
        while stack[move[2]-1][j] == '0' or stack[move[2]-1][j] == '0.0':
            j += 1
    to_move = stack[move[1]-1][i:i+move[0]]
    for c in reversed(to_move):
        if j == 0:
            stack[move[2]-1] = np.insert(stack[move[2]-1], 0, c)
        else:
            stack[move[2]-1][j-1] = c
            j -= 1
    for ind in range(i, i+move[0]):
        stack[move[1]-1][ind] = '0'
    return

for move in moves:
    do_move2(move, arr)
for s in range(len(arr)):
    i = 0
    while arr[s][i] == '0':
        i +=1
    print('stack ', s, ' has crate ', arr[s][i], ' on top.')
