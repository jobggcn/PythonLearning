#Excercise 2 Chapter 11 
#Image Site Downloader 

# main image links seem to follow the pattern 'a img' 
import requests, bs4, os
import pprint

website = 'http://imgur.com'
folder = '/home/oliver/test_tnails' 

def get_thumbnail_links(website): #imgur.com only right now 
    imgur_source = requests.get(website)
    imgur_bs4 = bs4.BeautifulSoup(imgur_source.text)
    image_elements = imgur_bs4.select('a img')
    return [image.attrs['src'] for image in image_elements] 

def download_thumbnail_images(images,folder):
    for image in images: 
        image_link = 'http:' + image 
        image_data = requests.get(image_link) 
        image_file = open(os.path.join(folder, os.path.basename(image)), 'wb')
        for chunk in image_data.iter_content(10000):
            image_file.write(chunk) 
        image_file.close() 

links = get_thumbnail_links(website) 
download_thumbnail_images(links,folder)
