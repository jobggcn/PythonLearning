#Excercise 1 Chapter 1 
#Extending the Multiclipboard 
import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb') 

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete': #keyword delete
    del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.arv[1].lower() == 'delete': #full delete
        for item in mcbShelf:
            del mcbShelf[item]
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
