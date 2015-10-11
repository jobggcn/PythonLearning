#Excercise 4 Chapter 12 
#Text Files To Spreadsheet 

import openpyxl, os, sys 

def write_spreadsheet(sheet_name, file_paths):
    workbook = openpyxl.Workbook() 
    sheet = workbook.get_active_sheet()
    
    
    for file_path in file_paths:
        text_file = open(file_path,'r') 
        lines = text_file.readlines()        
        for line in lines:
            sheet.cell(row = lines.index(line) + 1, column = file_paths.index(file_path) + 1).value = line 

    workbook.save(sheet_name) 
            
        
        


#lots of input validation logic for a little function 
if len(sys.argv) >= 3:
    sheet_name = sys.argv[1] 
    
    #Check supplied file paths 
    file_paths = []
    invalid_file_paths = [] 
    for file_path in sys.argv[2:len(sys.argv)]:
        if os.path.isfile(file_path) and file_path.endswith('.txt'):
            file_paths.append(file_path)
        else: 
            invalid_file_paths.append(file_path)
            
    #Error: Invalid File Paths
    if len(invalid_file_paths) > 0:
        print('Invalid text file paths:') 
        for file_path in invalid_file_paths:
            print(file_path)
    #Error: Invalid Spreadsheet Name 
    elif not sheet_name.endswith('.xlsx'):
        print('Spreadsheet name needs to end with .xlsx') 
    
    else:
        write_spreadsheet(sheet_name, file_paths) 
else: 
    print('python3 txtfilestoxlsx.py <spreadsheet path> <textfile 1> <textfile 2>...<textfile n>') 
            
