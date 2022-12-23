import numpy as np

directories = {'/': {'size':[], 'daughters': [], 'updated': [], 'level': 0}}
def add_dir(path, directory):
    name = path+'-'+directory
    directories[name] = {}
    directories[name]['size'] = []
    directories[name]['daughters'] = []
    directories[path]['daughters'] = np.append(directories.get(path).get('daughters'), directory)
    directories[name]['updated'] = []
    directories[name]['level'] = 0


def add_file(path, file_size):
    directories[path]['size'] = np.append(directories.get(path).get('size'), file_size)


def navigate(command, current):
    command = command.strip('\n')
    if command.startswith('$'):
        command = command.split(' ')
        if command[1] == 'ls':
            # print('ls', current)
            pass 
        elif command[1] == 'cd':
            if '.' in command[2]:
                if current == '/':
                    pass
                else:
                    parent = current.rsplit('-', 1)[0]
                    current = parent
                    # print('go up to', current)
            elif command[2] == '/':
                current = '/'
            else:
                folder = command[2]
                new = current+'-'+folder
                # print('go in from ', current, 'to', new)
                current = new
    elif command.startswith('dir'):
        name = command.split(' ')[1]
        fname = current+'-'+name
        if fname not in list(directories.keys()):
            add_dir(current, name)
            # print('added directory', name)
        else:
            print('directory already exists with', current+'-'+name)
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
    parent = folder.rsplit('-', 1)[0]
    directories.get(parent).get('updated').append(folder)
    add_file(parent, directories.get(folder).get('size'))
    return parent

def assign_level(folder, level):
    for d in directories.get(folder).get('daughters'):
        da = folder+'-'+d
        directories[da]['level'] = level+1
    level += 1
    return level

with open('/mnt/c/Users/Uni/Documents/GitHub/Advent/input_day7.txt', 'r') as file:
    c_folder = '/-/'
    for line in file:
        c_folder = navigate(line, c_folder)

# determine folders with size <= 100,000
len0 = []
level = 0
for f in list(directories.keys()):
    level = assign_level(f, level)
    if len(directories.get(f).get('daughters')) == 0:
        len0.append(f)
maxs = [directories.get(key).get('level') for key in directories]
max_level = max(maxs)
# sort directories by level
directories = dict(sorted(directories.items(), key=lambda item: item[1]['level']))
for f in list(reversed(directories.keys()))[0:-1]:  # update parent folder size from lowest level up to /
    parent = update_parent(f)
for folder in list(reversed(directories.keys())):  # update total size of folders
    directories = update_size(folder)

smalls = []
total = []
for f in directories.keys():
    if directories.get(f).get('size') <= 100000:
        smalls.append(f)
        total.append(directories.get(f).get('size'))
print(sum(total))
