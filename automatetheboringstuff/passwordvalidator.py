#Excercise 1 Chapter 7 
#Strong Password Detection 

import re 

def isStrongPw(password):
    is_8_long = re.compile(r'.{8}')
    has_uppercase = re.compile(r'[A-Z]')
    has_lowercase = re.compile(r'[a-z]') 
    has_digit = re.compile(r'\d') 
    
    return (is_8_long.search(password) and \
    has_uppercase.search(password) and \
    has_lowercase.search(password) and \
    has_digit.search(password)) is not None  

print(isStrongPw(''))
