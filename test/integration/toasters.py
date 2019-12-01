from test_functions import *
import pygame
from threading import Thread
import random
from PIL import Image, ImageDraw, ImageFont
from IT8951 import constants
from sys import path
path += ['../../']
from IT8951.display import AutoEPDDisplay

print('Initializing EPD...')
display = AutoEPDDisplay(vcom=-2.06)
print('VCOM set to', display.epd.get_vcom())

# load sprites
img1_path = 'sprite/toaster_01.png'
img2_path = 'sprite/toaster_02.png'
img3_path = 'sprite/toaster_03.png'
img4_path = 'sprite/toaster_04.png'
toast_path = 'sprite/toast.png'
print('Displaying Sprites')

# clearing image to black
display.clear()
display.frame_buf.paste(0x00, box=(0, 0, display.width, display.height))
print('Clearing screen to black')

img1 = Image.open(img1_path)
img2 = Image.open(img2_path)
img3 = Image.open(img3_path)
img4 = Image.open(img4_path)
toast = Image.open(toast_path)

# TODO: this should be built-in
dims = (display.width, display.height)

# Animation Variables
shift = 10

def toastersprite(randomstart):
    start = randomstart
    hor = start
    ver = -100
    while hor > -220:
    
        img1.thumbnail(dims)
        paste_coords = hor, ver
        display.frame_buf.paste(img1, paste_coords)
        display.draw_partial(constants.DisplayModes.DU)
    
        hor = hor - shift
        ver = ver + shift
        print(f'toaster position {hor},{ver}')
    
        img2.thumbnail(dims)
        paste_coords = hor, ver
        display.frame_buf.paste(img2, paste_coords)
        display.draw_partial(constants.DisplayModes.DU)
    
        hor = hor - shift
        ver = ver + shift
    
        img3.thumbnail(dims)
        paste_coords = hor, ver
        display.frame_buf.paste(img3, paste_coords)
        display.draw_partial(constants.DisplayModes.DU)
    
        hor = hor - shift
        ver = ver + shift
    
        img4.thumbnail(dims)
        paste_coords = hor, ver
        display.frame_buf.paste(img4, paste_coords)
        display.draw_partial(constants.DisplayModes.DU)
    
        hor = hor - shift
        ver = ver + shift
    
        img3.thumbnail(dims)
        paste_coords = hor, ver
        display.frame_buf.paste(img3, paste_coords)
        display.draw_partial(constants.DisplayModes.DU)
    
        hor = hor - shift
        ver = ver + shift
    
        img2.thumbnail(dims)
        paste_coords = hor, ver
        display.frame_buf.paste(img2, paste_coords)
        display.draw_partial(constants.DisplayModes.DU)
    
        hor = hor - shift
        ver = ver + shift

def toastsprite(randomstart):
    start = randomstart
    hor = start
    ver = -100
    while hor > -220:
    
        toast.thumbnail(dims)
        paste_coords = hor, ver
        display.frame_buf.paste(toast, paste_coords)
        display.draw_partial(constants.DisplayModes.DU)
        
        hor = hor - shift
        ver = ver + shift
        
# animating the display
x = 1
while True:
    randomstart = random.randint(1,801)
    print(f'toast starting position: {randomstart}')
    toastsprite(randomstart)
    print(f'toaster starting position: {randomstart}')
    toastersprite(randomstart)
