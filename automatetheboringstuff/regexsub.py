#Excercise 2 Chapter 7 
#Regex Version of strip() 
import re 

def regex_strip(s,sub = r"\s"):
    s = re.sub('^'+sub+r'*','',s)
    s = re.sub(sub+'*$','',s) 
    return s

print(regex_strip("   ssssss   ")) #Case 1 no substitution specified
print(regex_strip("ssssskkkkkssss",'s')) #Case 2 's' to be substituted 
print(regex_strip("9129921xxxx129291",r'\d')) #also does groups
