#Excercise 2 Chapter 15
#Webcomic downloader

import os, sys, requests, bs4, shelve
from urllib.parse import urljoin

image_folder = '/home/oliver/Desktop/Webcomics' 
if not os.path.isdir(image_folder): 
    os.makedir(image_folder) 

shelf_path = os.path.join(image_folder, 'persistent') 
last_downloads = shelve.open(shelf_path) 



def general_comic_downloader(comic_name, comic_url, css_selector):
    print(comic_name) 
    comic = requests.get(comic_url) 
    comic_bs4 = bs4.BeautifulSoup(comic.text)
    image_link = comic_bs4.select(css_selector)[0].attrs['src']
    image_link = urljoin(comic_url, image_link) 
    print(image_link) 
    if not comic_name in last_downloads:
        last_downloads[comic_name] = '' 
    
    if not last_downloads[comic_name] == image_link:
        print("downloading comic") 
        comic_image = requests.get(image_link)
        output_file_path = os.path.join(image_folder, comic_name + os.path.basename(image_link))
        output_file = open(output_file_path, 'wb') 
        for chunk in comic_image.iter_content(10000):
            output_file.write(chunk) 
        output_file.close()
        last_downloads[comic_name] = image_link 
        

#To try downloading a comic via the general downloader function, add it to this table
# 'comic' : Name of the comic
# 'src' : Page where new comic shows up on 
# 'css_s' : CSS selector that selects the image tag containing the comic 
comics = [ 
{'comic':'xkcd', 'src': 'http://xkcd.com/', 'css_s': 'div#comic > img'},
{'comic':'smbc', 'src': 'http://smbc-comics.com/', 'css_s': '#comic'},
{'comic':'cad', 'src':'http://www.cad-comic.com/cad/', 'css_s': '#content img'},
{'comic':'prace', 'src':'http://www.pragerace.com/',  'css_s': '#cc-comic'},
{'comic':'ndec', 'src':'http://www.ndecomic.com/', 'css_s': '#cc-comic'},
{'comic':'gige','src':'http://www.girlgeniusonline.com/comic.php', 'css_s': '#comicbody > img'}
]
 
for comic in comics:
    general_comic_downloader(comic['comic'], comic['src'], comic['css_s'])

