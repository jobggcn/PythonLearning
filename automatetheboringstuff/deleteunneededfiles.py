#Exercise 2 Chapter 9 
#Deleting Unneeded Files 

import os, sys, time, humanize


def list_files(folder):
    files = []
    for dir_path, dir_names, file_names in os.walk(folder):
        for file_name in file_names:
            files.append((dir_path,file_name))
    return files 

def sort_files_by_size_and_recency(file_names):
    file_info = []
    for dir_path,file_name in file_names:
        file_path = os.path.join(dir_path,file_name)
        try:
            file_size = os.stat(file_path).st_size 
            last_access_time = os.stat(file_path).st_atime
            time_since_access = time.time() - last_access_time
            file_info.append(\
    (dir_path,file_name,file_size,time_since_access))
        except IOError:
            print('{} not found'.format(file_path))
    file_info.sort(key = lambda x: x[2],reverse = True)
    return file_info 

def print_file_info(files, number = 100):
    for current_file in files[0:number]:
        dir_path,file_name,file_size,last_access_time = current_file
        full_path = os.path.join(dir_path,file_name)
        file_size = humanize.naturalsize(file_size)
        last_access_time = humanize.naturaltime(last_access_time)
        print('Path:{}\n Filesize:{}, Last accessed:{}'.format(full_path,file_size,last_access_time))

if len(sys.argv) == 2: 
    script, path = sys.argv
    if os.path.isdir(path):
        files = list_files(path)
        file_info = sort_files_by_size_and_recencz(files)
        print_file_info(file_info)
    else:
        print("invalid folder path") 
else:
    print("deleteunneededfiles.py <path>") 

  
