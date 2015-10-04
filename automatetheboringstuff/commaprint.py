# Comma Code Chapter 4 Practice Project 1 

test_list = ['hello','world','how','is','it','going']


def comma_print(my_list):
    _output = "" 
    for element in my_list[0:-1]:
        _output += element + ", "
    _output += my_list[-1]
    return _output

print(comma_print(test_list))


#Simpler Method via ', '.join(test_list) 
