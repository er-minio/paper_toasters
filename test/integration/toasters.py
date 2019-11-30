from test_functions import *
from PIL import Image, ImageDraw, ImageFont
from IT8951 import constants
from sys import path
path += ['../../']

from IT8951.display import AutoEPDDisplay

print('Initializing EPD...')
display = AutoEPDDisplay(vcom=-2.06)
print('VCOM set to', display.epd.get_vcom())

# def display_image_8bpp(display):
img1_path = 'sprite/toaster_01.png'
img2_path = 'sprite/toaster_02.png'
img3_path = 'sprite/toaster_03.png'
img4_path = 'sprite/toaster_04.png'
print('Displaying Sprites')

# clearing image to black
display.frame_buf.paste(0x00, box=(0, 0, display.width, display.height))
print('Clearing screen to black')

img1 = Image.open(img1_path)
img2 = Image.open(img2_path)
img3 = Image.open(img3_path)
img4 = Image.open(img4_path)

# TODO: this should be built-in
dims = (display.width, display.height)

x = 1
hor = 800
ver = -45
while True:
    
    img1.thumbnail(dims)
    paste_coords = hor, ver
    display.frame_buf.paste(img1, paste_coords)
    display.draw_full(constants.DisplayModes.DU)
    
    hor = hor - 5
    ver = ver + 5
    print(f'position {hor},{ver}')
    
    img2.thumbnail(dims)
    paste_coords = hor, ver
    display.frame_buf.paste(img2, paste_coords)
    display.draw_full(constants.DisplayModes.DU)
    
    hor = hor - 5
    ver = ver + 5
    
    img3.thumbnail(dims)
    paste_coords = hor, ver
    display.frame_buf.paste(img3, paste_coords)
    display.draw_full(constants.DisplayModes.DU)
    
    hor = hor - 5
    ver = ver + 5
    
    img4.thumbnail(dims)
    paste_coords = hor, ver
    display.frame_buf.paste(img4, paste_coords)
    display.draw_full(constants.DisplayModes.DU)
    
    hor = hor - 5
    ver = ver + 5
    
    img3.thumbnail(dims)
    paste_coords = hor, ver
    display.frame_buf.paste(img3, paste_coords)
    display.draw_full(constants.DisplayModes.DU)
    
    hor = hor - 5
    ver = ver + 5
    
    img2.thumbnail(dims)
    paste_coords = hor, ver
    display.frame_buf.paste(img2, paste_coords)
    display.draw_full(constants.DisplayModes.DU)
    
    hor = hor - 5
    ver = ver + 5