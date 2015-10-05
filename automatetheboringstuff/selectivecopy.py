#Exercise 1 Chapter 9 
#Selective Copy 
import os, sys, shutil

def list_files(folder, extension):
    file_list = []
    for dir_path, dir_names, file_names in os.walk(folder):
        for file_name in file_names:
            if file_name.endswith(extension):
                file_list.append((dir_path,file_name))
    return file_list

def copy_files(file_list,destination):
    for file_path in file_list:
        dir_path, file_name = file_path
        print(file_name)
        shutil.copy(os.path.join(dir_path, file_name),destination)

if len(sys.argv) == 4:
    script, extension, source, destination = sys.argv
    if os.path.isdir(source):
        if not os.path.isdir(destination):
            os.makedirs(destination)
        files = list_files(source, extension)
        copy_files(files,destination) 
else:
    print("selectivecopy.py <extension> <source> <destination>")
