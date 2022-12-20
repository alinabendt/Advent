import re

counter = 0
with open('/mnt/c/Users/Uni/Documents/GitHub/Advent/input_day4.txt', 'r') as file:
    for line in file:
        line = line.strip()
        pair = [int(s) for s in re.findall(r'\d+', line)]
        if pair[0] == pair[2] == pair[1] == pair[3]:
            pass
        if pair[0] <= pair[2] and pair[1] >= pair[3]:
            counter +=1
        elif pair[0] >= pair[2] and pair[1] <= pair[3]:
            counter +=1
print(counter)

# part 2: how many overlap at all
counter = 0
with open('/mnt/c/Users/Uni/Documents/GitHub/Advent/input_day4.txt', 'r') as file:
    for line in file:
        line = line.strip()
        pair = [int(s) for s in re.findall(r'\d+', line)]
        if pair[0] == pair[2] == pair[1] == pair[3]:
            pass
        if pair[0] <= pair[2] and pair[1] >= pair[3]:  # special case pair 2 completely in pair 1
            counter +=1
        elif pair[0] >= pair[2] and pair[1] <= pair[3]:  # special case pair 1 completely in pair 2
            counter +=1
        elif pair[0] <= pair[2] <= pair[1] <= pair[3]:  # example 2 < 3 < 5 <= 5  pair: 2-5,3-5
            counter +=1
        elif pair[1] >= pair[3] >= pair[0] >= pair[2]:  # example 7 > 6 > 5 > 3 pair: 7-5,6-3
            counter +=1
print(counter)

