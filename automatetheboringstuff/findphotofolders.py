#Excercise 2 Chapter 17 
#Identify Photo Folders 


import os, sys
from PIL import Image 

photo_folders = [] 
for directory, sub_directories, files in os.walk('/'):
    photo_files = [] 
    os.chdir(directory)
    for _file in files:
        print('Checking: {}'.format(_file))
        if _file.endswith('.png') or _file.endswith('.jpg') or _file.endswith('.jpeg'):
            try:
                image = Image.open(_file)
                width, height = image.size
                if width > 500 and height > 500:
                    photo_files.append(_file)
            except IOError:
                print('{} may be broken symbolic link'.format(_file))
    if len(photo_files) > len(files) / 0.5:
        photo_folders.append(os.path.abspath(directory))

for directory in photo_folders:
    print(directory)
