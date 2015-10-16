#Excercise 3 Chapter 17
#Greeting card generator 

import os, sys
from PIL import Image, ImageDraw, ImageFont

gc_width, gc_height = 360, 288 #4x5in Greeting Card 
guest_list_path = 'guests.txt'
bg_image = Image.open('floweryimage.jpeg')
bg_image = bg_image.resize((gc_width, gc_height), Image.ANTIALIAS) 
font_path = '/usr/share/fonts/truetype/tlwg/Sawasdee.ttf' 
name_font = ImageFont.truetype(font_path, 50)
invitation_font = ImageFont.truetype(font_path,20)
with open(guest_list_path) as guest_file:
    guests = guest_file.readlines() 

def generate_greeting_card(guest):
    cardImage = bg_image.copy() 
    draw = ImageDraw.Draw(cardImage)
    draw.text((100,50), guest, font= name_font, fill='black')
    draw.text((100,120), 'You are cordially invited to', font = invitation_font, fill = 'darkgrey')
    draw.text((200,150), 'CELEBRATION', font= invitation_font, fill = 'black')
    draw.text((200,200), 'Sincerely', font= invitation_font, fill = 'black')
    draw.line([(0,0),(0,gc_height-1),(gc_width-1,gc_height-1),(gc_width-1,0),(0,0)],fill = 'black')
    cardImage.save('{}_card.png'.format(guest)) 

for guest in guests:
    generate_greeting_card(guest)
