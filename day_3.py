import numpy as np
import string

dic = {}
for l in range(1, 27):
    dic[list(string.ascii_lowercase)[l-1]] = l
for l in range(27, 53):
    dic[list(string.ascii_uppercase)[l-27]] = l

priorities = 0
with open('/mnt/c/Users/Uni/Documents/GitHub/Advent/input_day3.txt', 'r') as file:
    for line in file:
        size = len(line)
        comp1 = line[0:int(size/2)]
        comp2 = line[int(size/2):]
        content = list(set(comp1)&set(comp2))
        common = [i for i in content]
        priorities = priorities + dic[common[0]]
print(priorities)

# part 2: common item within each set of three lines
priorities = 0
file = open('/mnt/c/Users/Uni/Documents/GitHub/Advent/input_day3.txt', 'r')
lines = file.readlines()
for count, line in enumerate(lines):
    pass
for l in range(count+1):
    lines[l] = lines[l][:-1]

for l in range(0, count+1, 3):
    pack1 = lines[l]
    pack2 = lines[l+1]
    pack3 = lines[l+2]
    content = list(set(pack1)&set(pack2)&set(pack3))
    common = [i for i in content]
    priorities = priorities + dic[common[0]]
print(priorities)

