#Excercise 3 Chapter 8 
#Regex Folder Search 

import re, os, sys
import pprint

def list_txt_files(folder):
    list_of_files = [] 
    for dir_path, dir_names, file_names in os.walk(folder):
        for file_name in file_names:
            if file_name.endswith('.txt'):
                list_of_files.append(\
                    os.path.join(dir_path,file_name))
    return list_of_files

def search_files(file_names, regex):
    #Returns (line, match, file, line#, position)  
    search_regex = re.compile(regex)
    matches = []
    for file_name in file_names:
        open_file = open(file_name,'r')
        lines = open_file.readlines() 
        open_file.close() 
        for line in lines:
            for match in search_regex.finditer(line):
                match_line = line[0:15] + "(...)"
                match_content = match.group()
                match_file = os.path.basename(file_name)
                match_line_nr = lines.index(line) 
                match_pos_start = match.start()
                match_pos_end = match.end() 
                matches.append(\
(match_line, match_content, match_file, match_line_nr,\
 match_pos_start,match_pos_end)) 
    
    return matches 

def print_matches(matches):
    for match in matches:
        print('''Line:"{}" Match:"{}", File:"{}", Line#:"{}", Start:"{}", End: "{}"'''.format(*match))

#MAIN!!!!
if len(sys.argv) == 3:
    script, regex, path = sys.argv
    files = list_txt_files(path)
    matches = search_files(files,regex) 
    print_matches(matches) 
else:
    print('python3 regexsearch.py <regex> <path>')
