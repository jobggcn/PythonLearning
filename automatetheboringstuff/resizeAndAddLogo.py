#Excercise 1 Chapter 17
#Extending and fixing the chapter project 

SQUARE_FIT_SIZE = 300 
LOGO_FILENAME = 'catlogo.png' 

logoIm = Image.open(LOGO_FILENAME)
logoWidht, logoHeight = logoIm.size

for filename in os.listdir('.'):
    if not ((filename.lower().endswith('.png') 
        or filename.lower().endswith('.jpg'))
        or filename == LOGO_FILENAME):
        continue #skip non image files and the logo file itself
    
    im = Image.open(filename) 
    width, height = im.size
    large_enough = width > logoWidth*2 and height  > logoHeight*2 

    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
    # Resize the image 
    print('Resizing {}...'.format(filename))
    im = im.resize((width, height))
    # Add the logo
    if large_enough:
        print('Adding logo to {}'.format(filename)) 
        im.paste(logoIm, (width - logoWidht, height - logoHeight), logoIm)
    # Save changes 
    im.save(os.path.join('widthLogo', filename)) 
