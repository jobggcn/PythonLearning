#Exercise 3 Chapter 9 
#Filling in the gaps 

import os, sys, re, shutil
import pprint 

def list_files(directory,prefix):
    files = os.listdir(directory)
    filter_regex = re.compile(prefix + r'\d+\.txt')
    files = list(filter(lambda x: filter_regex.search(x),files)) 
    return files 

def reorder_files(directory, prefix, files):
    files.sort(key = lambda x: \
               int(re.search('(\d+)\.txt',x).group(1)))
    for current_file in files:
        old_path = os.path.join(directory, current_file)
        new_path = os.path.join(directory, \
            prefix + str(files.index(current_file)) + '.txt')
        
        shutil.move(old_path,new_path)
        print('Renamed "{}" to "{}"'.format(old_path,new_path))
    print("Reordered {} files".format(len(files)))

if len(sys.argv) == 3:
    if os.path.isdir(sys.argv[1]):
        files = list_files(sys.argv[1],sys.argv[2])
        reorder_files(sys.argv[1],sys.argv[2],files)
    else:
        print("invalid folder path")
else:
    print("filerenumber.py <path> <prefix>") 
