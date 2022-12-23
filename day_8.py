import numpy as np

grid = []
with open('/mnt/c/Users/Uni/Documents/GitHub/Advent/input_day8.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        line = [int(s) for s in line]
        grid.append(line)
grid = np.asarray(grid)

visible = (np.shape(grid)[0]*2) + ((np.shape(grid)[1]-2)*2)
# add any trees that are inside the grid that are visible from outside
for i in range(1, np.shape(grid)[0]-1):
    for j in range(1, np.shape(grid)[1]-1):
        v = False
        # visible from left
        if all(trees < grid[i,j] for trees in grid[i, 0:j]):
            v = True
        # visible from right
        elif all(trees < grid[i,j] for trees in grid[i, j+1:]):
            v = True
        # visible from top
        elif all(trees < grid[i,j] for trees in grid[0:i, j]):
            v = True
        # visible from bottom
        elif all(trees < grid[i,j] for trees in grid[i+1:, j]):
            v = True
        if v is True:
            visible += 1
print(visible)

# part 2: scenic score = multiply number of trees visiblein any direction from tree
def scenic(tree, direction):
    x = 0
    for t in direction:
        if t < tree:
            x +=1
        elif t == tree:
            x +=1
            return x
        elif t > tree:
            return x
    return x


score = np.zeros(np.shape(grid))
for i in range(np.shape(grid)[0]):
    for j in range(np.shape(grid)[1]):
        l = scenic(grid[i,j], reversed(grid[i, 0:j]))
        r = scenic(grid[i,j], grid[i, j+1:])
        t = scenic(grid[i,j], reversed(grid[0:i, j]))
        b = scenic(grid[i,j], grid[i+1:, j])
        score[i,j] = l*r*t*b
# find max
max_score = np.max(score)
print(max_score)
