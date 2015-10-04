# Character Picture Grid 
# Exercise 2 Chapter 4 

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


def print_square(grid):
    width = len(grid)
    height = max([len(column) for column in grid]) 
    for h_index in range(height):
        line = "" 
        for w_index in range(width):
            if h_index >=  len(grid[w_index]):
                line += ' ' 
            else:
                line += grid[w_index][h_index]
        print(line)


        

print_square(grid)
