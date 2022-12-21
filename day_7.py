import numpy as np

directories = {'/': {'parent': '/', 'size':[], 'daughters': []}}
def add_dir(parent, directory):
    directories[directory] = {}
    directories[directory]['parent'] = parent
    directories[directory]['size'] = []
    directories[directory]['daughters'] = []
    directories[parent]['daughters'] = np.append(directories.get(parent).get('daughters'), directory)

def add_file(directory, file_size):
    directories[directory]['size'] = np.unique(np.append(directories.get(directory).get('size'), file_size))


def navigate(command, current):
    command = command.strip('\n')
    if command.startswith('$'):
        command = command.split(' ')
        if command[1] == 'ls':
            # print('ls', current)
            pass 
        elif command[1] == 'cd':
            if '.' in command[2]:
                parent = directories.get(current).get('parent')
                current = parent
                # print('go up to', current)
            else:
                folder = command[2]
                current = folder
                # print('go in to', folder)
    elif command.startswith('dir'):
        name = command.split(' ')[1]
        if name not in list(directories.keys()):
            add_dir(current, name)
        # print('add dir', name, current)
    elif command[0].isdigit():
        folder = current
        size = int(command.split(' ')[0])
        add_file(folder, size)
        # print('add file', folder, size)
    return current

def update_size(folder):
    directories.get(folder)['size'] = sum(directories.get(folder).get('size'))
    return directories

def update_parent(folder):
    parent = directories.get(folder).get('parent')
    add_file(parent, directories.get(folder).get('size'))
    return parent

with open('/mnt/c/Users/Uni/Documents/GitHub/Advent/input_day7.txt', 'r') as file:
    c_folder = '/'
    for line in file:
        c_folder = navigate(line, c_folder)

# determine folders with size <= 100,000
len0 = []
for f in list(directories.keys()):
    if len(directories.get(f).get('daughters')) == 0:
        len0.append(f)
for f in len0:
    folder = f
    while folder != '/':
        parent = update_parent(folder)
        folder = parent
print('updated parents:', directories)
for folder in list(reversed(directories.keys())):
    directories = update_size(folder)
print('summed:', directories)

smalls = []
total = []
for f in directories.keys():
    if directories.get(f).get('size') <= 100000:
        smalls.append(f)
        total.append(directories.get(f).get('size'))
print(sum(total))
