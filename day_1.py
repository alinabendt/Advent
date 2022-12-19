import numpy as np

cal = 0
counter = 0
elves = {}
with open("/mnt/c/Users/Uni/Documents/GitHub/Advent/day_1_in.txt", 'r') as file:
    for line in file:
        if line.strip():
            cal = cal+int(line)
        else:
            elves[counter] = cal
            cal = 0
            counter += 1
# find elf with most calories
max_cal = 0
max_elf = 0
for key in elves:
    if elves[key] > max_cal:
        max_cal = elves[key]
        max_elf = key
print(max_elf, max_cal)

# part 2: find top three elfs with most cal
elf_sorted = sorted(elves.items(), key= lambda x:x[1], reverse=True)
print('top three elves: ', elf_sorted[0:3])
tot_cal = [elf_sorted[i][1] for i in range(3)]
total = np.sum(tot_cal)
print(total)
