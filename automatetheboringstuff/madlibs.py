#Excercise 2 Chapter 8 
#Mad Libs 

import re, os, sys

def replace_words(text):
    mlibs_regex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
    print(text)
    while mlibs_regex.search(text):
        match = mlibs_regex.search(text) 
        prompt = 'Please enter a/an {} :\n'.format(match.group().lower())
        substitution = input(prompt) 
        text = mlibs_regex.sub(substitution,text,count=1) 
    return text 

if len(sys.argv) == 2:
    file_path = sys.argv[1]
    if os.path.isfile(file_path):
        #Read File and Edit Text
        open_file = open(file_path,'r')
        text = ''.join(open_file.readlines())
        text = replace_words(text)
        open_file.close()
        #Write Text to File 
        open_file = open(file_path,'w')
        open_file.write(text) 
        open_file.close() 
    else:
        print('Cannot find "{}"'.format(sys.argv[1])) 
else: 
    print('python3 madlibs.py <file path>') 
  
