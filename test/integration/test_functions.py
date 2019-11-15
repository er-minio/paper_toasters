'''
This file contains various functions to test different aspects
of the module's display capabilities. Each function takes only
an AutoDisplay object (or, probably, an object of a type derived 
from that class) as an argument, so they can be used with either
an actual AutoEPDDisplay, or a VirtualEPDDisplay, or something else.

See test.py for an example. 
'''

# functions defined in this file
__all__ = [
    'print_system_info',
    'clear_display',
    'display_gradient',
    'display_image_8bpp',
    'partial_update'
]

from PIL import Image, ImageDraw, ImageFont

from sys import path
path += ['../../']
from IT8951 import constants

def print_system_info(display):
    epd = display.epd

    print('System info:')
    print('  display size: {}x{}'.format(epd.width, epd.height))
    print('  img buffer address: {:X}'.format(epd.img_buf_address))
    print('  firmware version: {}'.format(epd.firmware_version))
    print('  LUT version: {}'.format(epd.lut_version))
    print()

def clear_display(display):
    print('Clearing display...')
    display.clear()

def display_gradient(display):
    print('Displaying gradient...')

    # set frame buffer to gradient
    for i in range(16):
        color = i*0x10
        box = (
            i*display.width//16,      # xmin
            0,                        # ymin
            (i+1)*display.width//16,  # xmax
            display.height            # ymax
        )
        
        display.frame_buf.paste(color, box=box)

    # update display
    display.draw_full(constants.DisplayModes.GC16)

def display_image_8bpp(display):
    img1_path = 'sprite/toaster_01.png'
    img2_path = 'sprite/toaster_02.png'
    img3_path = 'sprite/toaster_03.png'
    img4_path = 'sprite/toaster_04.png'
    print('Displaying Sprites')

    # clearing image to white
    display.frame_buf.paste(0xFF, box=(0, 0, display.width, display.height))

    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)
    img3 = Image.open(img3_path)
    img4 = Image.open(img4_path)

    # TODO: this should be built-in
    dims = (display.width, display.height)

    x = 1
    while True:
        
        img1.thumbnail(dims)
        paste_coords = 350,200
        display.frame_buf.paste(img1, paste_coords)
        display.draw_full(constants.DisplayModes.DU)
        
        img2.thumbnail(dims)
        paste_coords = 350,200
        display.frame_buf.paste(img2, paste_coords)
        display.draw_full(constants.DisplayModes.DU)
        
        img3.thumbnail(dims)
        paste_coords = 350,200
        display.frame_buf.paste(img3, paste_coords)
        display.draw_full(constants.DisplayModes.DU)
        
        img4.thumbnail(dims)
        paste_coords = 350,200
        display.frame_buf.paste(img4, paste_coords)
        display.draw_full(constants.DisplayModes.DU)
        
        img3.thumbnail(dims)
        paste_coords = 350,200
        display.frame_buf.paste(img3, paste_coords)
        display.draw_full(constants.DisplayModes.DU)
        
        img2.thumbnail(dims)
        paste_coords = 350,200
        display.frame_buf.paste(img2, paste_coords)
        display.draw_full(constants.DisplayModes.DU)
        

def partial_update(display):
    print('Starting partial update...')

    # clear image to white
    display.frame_buf.paste(0xFF, box=(0, 0, display.width, display.height))

    print('  writing full...')
    _place_text(display.frame_buf, 'partial', x_offset=-200)
    display.draw_full(constants.DisplayModes.GC16)

    # TODO: should use 1bpp for partial text update
    print('  writing partial...')
    _place_text(display.frame_buf, 'update', x_offset=+200)
    display.draw_partial(constants.DisplayModes.DU)

# this function is just a helper for the others
def _place_text(img, text, x_offset=0, y_offset=0):
    '''
    Put some centered text at a location on the image.
    '''
    fontsize = 80

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSans.ttf', fontsize)

    img_width, img_height = img.size
    text_width, _ = font.getsize(text)
    text_height = fontsize

    draw_x = (img_width - text_width)//2 + x_offset
    draw_y = (img_height - text_height)//2 + y_offset

    draw.text((draw_x, draw_y), text, font=font)
