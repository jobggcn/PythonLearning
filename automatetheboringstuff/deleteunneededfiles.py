#Exercise 2 Chapter 9 
#Deleting Unneeded Files 

import os, sys, time 

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
        last_opened = os.stat(file_path).st_atime
        elapsed_time = time.time() - float(last_opened)
        file_size = os.stat(file_path).st_size 
        score = file_size * elapsed_time
        file_info.append((dir_path, file_name, elapsed_time, file_size, score))

    file_info.sort(key=lambda score: score[4])
    for result in file_info[0:100]:
       print(result[1])

files = list_files(r"./")
sort_files_by_size_and_recency(files)
