"""

Дано папку і шлях до файлу. Необхідно перевірити наявність файлу у даній
папці
"""

import re
print(''.join(['c', 'd']))
def joiner(folder):
    for subfolder in folder:
        if isinstance(subfolder, list):
            subfolder = joiner(subfolder)
    return ''.join(folder)

print(joiner(['g',['k']]))

def file_search(folder, file_path):
    """

    :param folder: list, first element is the folder name, ['C:', 'temp.zip']
    :param file_path: str, must contain folder name with the file name, folder0/file.txt
    :return: str, OK or ERROR
    """
    files = re.split(r'/', file_path)

    directory = joiner(folder)
    print(directory)
    for file in files:
        if not re.search(file, directory):
            print('ERROR')
            break
    return print('OK')
file_search(['C:', 'ideas.txt'], 'C:/ideas.txt')
file_search(['D:',['recycle.bin'], ['tmp',['old'],['new folder1', 'asd.txt', 'asd.bak', 'find.me.bak']], 'het.py'], 'D:/tmp/new folderX')
