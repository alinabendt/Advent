import numpy as np

class heta():
    history = [[0, 0]]
    def __init__(self, pos):
        self.pos = pos

    def move(self, steps):
        pos_h = self.pos
        if steps[0] == 'R':
            pos_h[1] = self.pos[1]+1
        elif steps[0] == 'L':
            pos_h[1] = self.pos[1]-1
        elif steps[0] == 'U':
            pos_h[0] = self.pos[0]-1
        elif steps[0] == 'D':
            pos_h[0] = self.pos[0]+1
        self.pos = pos_h
        self.history = np.append(self.history, [self.pos], axis=0)
        return pos_h
    def move_t(self, head):
        if head[1] == self.pos[1]:  # head and tail in same column
            if head[0]-self.pos[0] == -2:  # head is two steps above
                self.pos[0] = self.pos[0]-1
            elif head[0]-self.pos[0] == 2:  # head is two steps below
                self.pos[0] = self.pos[0]+1
        elif head[0] == self.pos[0]:  # head and tail in same row
            if head[1]-self.pos[1] == -2:  # head is two steps left
                self.pos[1] = self.pos[1]-1
            elif head[1]-self.pos[1] == 2:  # head is two steps right
                self.pos[1] = self.pos[1]+1
        # diagonal cases
        elif head[1]-self.pos[1] == 2 and head[0]-self.pos[0] == -1:
            self.pos = [self.pos[0]-1, self.pos[1]+1]
        elif head[1]-self.pos[1] == 2 and head[0]-self.pos[0] == 1:
            self.pos = [self.pos[0]+1, self.pos[1]+1]
        elif head[1]-self.pos[1] == -2 and head[0]-self.pos[0] == -1:
            self.pos = [self.pos[0]-1, self.pos[1]-1]
        elif head[1]-self.pos[1] == -2 and head[0]-self.pos[0] == 1:
            self.pos = [self.pos[0]+1, self.pos[1]-1]
        elif head[0]-self.pos[0] == 2 and head[1]-self.pos[1] == -1:
            self.pos = [self.pos[0]+1, self.pos[1]-1]
        elif head[0]-self.pos[0] == 2 and head[1]-self.pos[1] == 1:
            self.pos = [self.pos[0]+1, self.pos[1]+1]
        elif head[0]-self.pos[0] == -2 and head[1]-self.pos[1] == -1:
            self.pos = [self.pos[0]-1, self.pos[1]-1]
        elif head[0]-self.pos[0] == -2 and head[1]-self.pos[1] == 1:
            self.pos = [self.pos[0]-1, self.pos[1]+1]
        elif head[0]-self.pos[0] == 2 and head[1]-self.pos[1] == 2:
            self.pos = [self.pos[0]+1, self.pos[1]+1]
        elif head[0]-self.pos[0] == -2 and head[1]-self.pos[1] == -2:
            self.pos = [self.pos[0]-1, self.pos[1]-1]
        elif head[0]-self.pos[0] == 2 and head[1]-self.pos[1] == 2:
            self.pos = [self.pos[0]+1, self.pos[1]+1]
        elif head[0]-self.pos[0] == -2 and head[1]-self.pos[1] == 2:
            self.pos = [self.pos[0]-1, self.pos[1]+1]
        elif head[0]-self.pos[0] == 2 and head[1]-self.pos[1] == -2:
            self.pos = [self.pos[0]+1, self.pos[1]-1]
        self.history = np.append(self.history, [self.pos], axis=0)
        return self.pos

Head = heta([0,0])
Tail = heta([0,0])

with open('/mnt/c/Users/Uni/Documents/GitHub/Advent/input_day9.txt', 'r') as file:
    for line in file:
        command = line.strip('\n')
        command = command.split(' ')
        for _ in range(int(command[1])):
            Head.pos = Head.move(command)
            Tail.pos = Tail.move_t(Head.pos)
no_tail = np.shape(np.unique(Tail.history, axis=0))[0]
print('the tail visited ', no_tail, ' positions')

# part 2
Head = heta([0,0])
Knot1 = heta([0,0])
Knot2 = heta([0,0])
Knot3 = heta([0,0])
Knot4 = heta([0,0])
Knot5 = heta([0,0])
Knot6 = heta([0,0])
Knot7 = heta([0,0])
Knot8 = heta([0,0])
Knot9 = heta([0,0])
with open('/mnt/c/Users/Uni/Documents/GitHub/Advent/input_day9.txt', 'r') as file:
    for line in file:
        command = line.strip('\n')
        command = command.split(' ')
        for _ in range(int(command[1])):
            Head.pos = Head.move(command)
            Knot1.pos = Knot1.move_t(Head.pos)
            Knot2.pos = Knot2.move_t(Knot1.pos)
            Knot3.pos = Knot3.move_t(Knot2.pos)
            Knot4.pos = Knot4.move_t(Knot3.pos)
            Knot5.pos = Knot5.move_t(Knot4.pos)
            Knot6.pos = Knot6.move_t(Knot5.pos)
            Knot7.pos = Knot7.move_t(Knot6.pos)
            Knot8.pos = Knot8.move_t(Knot7.pos)
            Knot9.pos = Knot9.move_t(Knot8.pos)
no_tail = np.shape(np.unique(Knot9.history, axis=0))[0]
print('the Knot9 visited ', no_tail, ' positions')

