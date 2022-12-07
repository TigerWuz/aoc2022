from utils.inputReader import InputReader
from collections import namedtuple

File = namedtuple('File', ['name', 'size'])

root = None

solution_a_folders = []
solution_b_folderList = []

class Folder():
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.childDirectories = []
        self.files = []

    def addDir(self, folder):
        self.childDirectories.append(folder)

    def addFile(self, file):
        self.files.append(file)

    def get_total_filesize(self):
        total = 0
        for file in self.files:
            total = total + file.size
        return total
    
    def get_total_foldersize(self):
        global solution_folders
        global solution_b_folderList

        folder_size = self.get_total_filesize()
        for child in self.childDirectories:
            folder_size = folder_size + child.get_total_foldersize()

        if folder_size <= 100000:
            solution_a_folders.append(folder_size)

        solution_b_folderList.append(folder_size)

        return folder_size

def exec_command(command, currentFolder=None):
    # first element is '$' second is either cd or ls third is /, .. or a name in case of cd
    command = command.split(' ')

    global root
    result = None

    if command[1] == 'cd':
        if command[2] == '..':
            print("Going one level up..")
            result = currentFolder.parent
        elif command[2] == '/':
            print("Returning to root /")
            if root is None:
                root = Folder(None, 'root')
            
            result = root
        else:
            print("Entering directory: {}".format(command[2]))
            for child in currentFolder.childDirectories:
                if child.name == command[2]:
                    print('Entering existing folder {}'.format(command[2]))
                    result = child
                    break

            if result is None:
                print('ERROR: Folder \'{}\' does not exist.'.format(command[2]))
                result = currentFolder

    elif command[1] == 'ls':
        print("listing files")
        result = currentFolder
        
    return result

def day7():
    input = InputReader.get("input\\day7.txt")

    current_folder = None

    for line in input:
        if line.startswith('$'):
            current_folder = exec_command(line, current_folder)

        #result is the current folder we are in...
        elif line.startswith('dir'):
            _, name = line.split(' ')
            new_folder = Folder(parent = current_folder, name = name)
            current_folder.addDir(new_folder)

        else: # only files should be present here....
            file_size, file_name = line.split(' ')
            new_file = File(name=file_name, size=int(file_size))
            current_folder.addFile(new_file)

    # File system structure was created now we need to calculate the sizes
    result = root.get_total_foldersize()

    print('Solution 1: Sum of Directories below 100000: {}'.format(sum(solution_a_folders)))

    solution_b_folderList.sort()

    #find how much space needs to be freed up
    free_space = 70000000 - result
    needed_space = 30000000 - free_space

    for x in solution_b_folderList:
        if x > needed_space:
            print('Solution 2: Delete the folder with size {}'.format(x))
            break

day7()
