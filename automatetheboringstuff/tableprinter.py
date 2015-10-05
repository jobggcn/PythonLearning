#Exercise 1 Chapter 6 
import itertools 
tableData = [['apples', 'oranges', 'cherries', 'banana','pear'],
             ['Ace', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose','horse']]


def find_column_widths(table):
    #Turn strings into their lenghts 
    lenght_table = list(map(lambda x: list(map(len, x)),table))
    #Rotate the jagged array 
    inversion = list(map(list, itertools.zip_longest(\
    *lenght_table,fillvalue = 0)))
    #Find maximum value in column 
    column_widths = list(map(max, inversion))
    return column_widths 

def printTable(table):
    offset = 1
    column_widths = find_column_widths(table)
    for row in table:
        line = "" 
        for e_index in range(len(row)):
            line += row[e_index].rjust(column_widths[e_index]+offset)
        print(line) 
    
printTable(tableData)

