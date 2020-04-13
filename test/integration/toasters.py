import random
from PIL import Image, ImageDraw, ImageFont
from IT8951 import constants
from sys import path
path += ['../../']
from IT8951.display import AutoEPDDisplay
from itertools import chain

print('Initializing EPD...')
display = AutoEPDDisplay(vcom=-1.79)
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

# def toastersprite(randomstart):
#     start = randomstart
#     hor = start
#     ver = -100
#     delta = 200
#     while hor > -220:
#
#         img1.thumbnail(dims)
#         paste_coords = hor, ver
#         display.frame_buf.paste(img1, paste_coords)
#         display.draw_partial(constants.DisplayModes.DU)
#
#         #second_toaster
#         img1.thumbnail(dims)
#         paste_coords = hor-delta, ver-delta
#         display.frame_buf.paste(img1, paste_coords)
#         display.draw_partial(constants.DisplayModes.DU)
#
#         hor = hor - shift
#         ver = ver + shift
#         print(f'toaster position {hor},{ver}')
#
#         img2.thumbnail(dims)
#         paste_coords = hor, ver
#         display.frame_buf.paste(img2, paste_coords)
#         display.draw_partial(constants.DisplayModes.DU)
#
#         #second_toaster
#         img2.thumbnail(dims)
#         paste_coords = hor-delta, ver-delta
#         display.frame_buf.paste(img2, paste_coords)
#         display.draw_partial(constants.DisplayModes.DU)
#
#         hor = hor - shift
#         ver = ver + shift
#
#         img3.thumbnail(dims)
#         paste_coords = hor, ver
#         display.frame_buf.paste(img3, paste_coords)
#         display.draw_partial(constants.DisplayModes.DU)
#
#         #second_toaster
#         img3.thumbnail(dims)
#         paste_coords = hor-delta, ver-delta
#         display.frame_buf.paste(img3, paste_coords)
#         display.draw_partial(constants.DisplayModes.DU)
#
#         hor = hor - shift
#         ver = ver + shift
#
#         img4.thumbnail(dims)
#         paste_coords = hor, ver
#         display.frame_buf.paste(img4, paste_coords)
#         display.draw_partial(constants.DisplayModes.DU)
#
#         #second_toaster
#         img4.thumbnail(dims)
#         paste_coords = hor-delta, ver-delta
#         display.frame_buf.paste(img4, paste_coords)
#         display.draw_partial(constants.DisplayModes.DU)
#
#         hor = hor - shift
#         ver = ver + shift
#
#         img3.thumbnail(dims)
#         paste_coords = hor, ver
#         display.frame_buf.paste(img3, paste_coords)
#         display.draw_partial(constants.DisplayModes.DU)
#
#         #second_toaster
#         img3.thumbnail(dims)
#         paste_coords = hor-delta, ver-delta
#         display.frame_buf.paste(img3, paste_coords)
#         display.draw_partial(constants.DisplayModes.DU)
#
#         hor = hor - shift
#         ver = ver + shift
#
#         img2.thumbnail(dims)
#         paste_coords = hor, ver
#         display.frame_buf.paste(img2, paste_coords)
#         display.draw_partial(constants.DisplayModes.DU)
#
#         #second_toaster
#         img2.thumbnail(dims)
#         paste_coords = hor-delta, ver-delta
#         display.frame_buf.paste(img2, paste_coords)
#         display.draw_partial(constants.DisplayModes.DU)
#
#         hor = hor - shift
#         ver = ver + shift
#
# def toastsprite(randomstart):
#     start = randomstart
#     hor = start
#     ver = -100
#     while hor > -220:
#
#         toast.thumbnail(dims)
#         paste_coords = hor, ver
#         display.frame_buf.paste(toast, paste_coords)
#         display.draw_partial(constants.DisplayModes.DU)
#
#         hor = hor - shift
#         ver = ver + shift
        
def ensemble(randomstart):
    start1 = randomstartoaster1
    start2 = randomstartoaster2
    start3 = randomstartoast
    hor1 = start1
    hor2 = start2
    hor3 = start3
    ver = -100
    while hor1 > -220:
    
        img1.thumbnail(dims)
        paste_coords = hor1, ver
        display.frame_buf.paste(img1, paste_coords)
        display.draw_partial(constants.DisplayModes.DU)
       
        #second_toaster
        img1.thumbnail(dims)
        paste_coords = hor2, ver - delta
        display.frame_buf.paste(img1, paste_coords)
        display.draw_partial(constants.DisplayModes.DU)
        
        #toast
        toast.thumbnail(dims)
        paste_coords = hor3, ver - toastdelta
        display.frame_buf.paste(toast, paste_coords)
        display.draw_partial(constants.DisplayModes.DU)
        
        hor1 = hor1 - shift
        hor2 = hor2 - shift
        hor3 = hor3 - shift
        ver = ver + shift
        
        print(f'toaster1 position {hor1},{ver}')
        print(f'toaster2 position {hor2},{ver}')
        print(f'toast position {hor3},{ver}')
    
        img2.thumbnail(dims)
        paste_coords = hor1, ver
        display.frame_buf.paste(img2, paste_coords)
        display.draw_partial(constants.DisplayModes.DU)
        
        #second_toaster
        img2.thumbnail(dims)
        paste_coords = hor2, ver - delta
        display.frame_buf.paste(img2, paste_coords)
        display.draw_partial(constants.DisplayModes.DU)
        
        #toast
        toast.thumbnail(dims)
        paste_coords = hor3, ver - toastdelta
        display.frame_buf.paste(toast, paste_coords)
        display.draw_partial(constants.DisplayModes.DU)
    
        hor1 = hor1 - shift
        hor2 = hor2 - shift
        hor3 = hor3 - shift
        ver = ver + shift
    
        img3.thumbnail(dims)
        paste_coords = hor1, ver
        display.frame_buf.paste(img3, paste_coords)
        display.draw_partial(constants.DisplayModes.DU)
        
        #second_toaster
        img3.thumbnail(dims)
        paste_coords = hor2, ver - delta
        display.frame_buf.paste(img3, paste_coords)
        display.draw_partial(constants.DisplayModes.DU)
        
        #toast
        toast.thumbnail(dims)
        paste_coords = hor3, ver - toastdelta
        display.frame_buf.paste(toast, paste_coords)
        display.draw_partial(constants.DisplayModes.DU)
    
        hor1 = hor1 - shift
        hor2 = hor2 - shift
        hor3 = hor3 - shift
        ver = ver + shift
    
        img4.thumbnail(dims)
        paste_coords = hor1, ver
        display.frame_buf.paste(img4, paste_coords)
        display.draw_partial(constants.DisplayModes.DU)
        
        #second_toaster
        img4.thumbnail(dims)
        paste_coords = hor2, ver - delta
        display.frame_buf.paste(img4, paste_coords)
        display.draw_partial(constants.DisplayModes.DU)
        
        #toast
        toast.thumbnail(dims)
        paste_coords = hor3, ver - toastdelta
        display.frame_buf.paste(toast, paste_coords)
        display.draw_partial(constants.DisplayModes.DU)
    
        hor1 = hor1 - shift
        hor2 = hor2 - shift
        hor3 = hor3 - shift
        ver = ver + shift
    
        img3.thumbnail(dims)
        paste_coords = hor1, ver
        display.frame_buf.paste(img3, paste_coords)
        display.draw_partial(constants.DisplayModes.DU)
        
        #second_toaster
        img3.thumbnail(dims)
        paste_coords = hor2, ver - delta
        display.frame_buf.paste(img3, paste_coords)
        display.draw_partial(constants.DisplayModes.DU)
        
        #toast
        toast.thumbnail(dims)
        paste_coords = hor3, ver - toastdelta
        display.frame_buf.paste(toast, paste_coords)
        display.draw_partial(constants.DisplayModes.DU)
    
        hor1 = hor1 - shift
        hor2 = hor2 - shift
        hor3 = hor3 - shift
        ver = ver + shift
    
        img2.thumbnail(dims)
        paste_coords = hor1, ver
        display.frame_buf.paste(img2, paste_coords)
        display.draw_partial(constants.DisplayModes.DU)
        
        #second_toaster
        img2.thumbnail(dims)
        paste_coords = hor2, ver - delta
        display.frame_buf.paste(img2, paste_coords)
        display.draw_partial(constants.DisplayModes.DU)
        
        #toast
        toast.thumbnail(dims)
        paste_coords = hor3, ver - toastdelta
        display.frame_buf.paste(toast, paste_coords)
        display.draw_partial(constants.DisplayModes.DU)
    
        hor1 = hor1 - shift
        hor2 = hor2 - shift
        hor3 = hor3 - shift
        ver = ver + shift
        
# animating the display
x = 1
while True:
    
    #randomizing start point and detecting collisions
    randomstartoaster1 = random.randint(1,801)
    print(f'### toaster1 starting position: {randomstartoaster1}')
    randomstartoaster2 = random.randint(1,801)
    randomstartoast = random.randint(1,801)
    print(f'### toast starting position: {randomstartoast}')
    toastdelta = random.randint(1,801)
    print(f'### toast delta: {toastdelta}')
    delta = random.randint(1,801)
    print(f'### toaster delta: {delta}')
    toaster2_range = chain(range(randomstartoaster1-164, randomstartoaster1+164), range(randomstartoast-164, randomstartoast+164))
    toast_range = chain(range(randomstartoaster1-164, randomstartoaster1+164), range(randomstartoaster2-164, randomstartoaster2+164))
    
    while randomstartoaster2 in toaster2_range:
     print(f'### toaster2 collision: {randomstartoaster2} #############################################')
     randomstartoaster2 = random.randint(1,801)
     print('regenerating toaster2 origin')
    print(f'### adjusted toaster2 starting position: {randomstartoaster2}')
    
    while randomstartoast in toast_range:
     print(f'### toast collision: {randomstartoast} #############################################')
     randomstartoaster2 = random.randint(1,801)
     print('regenerating toast origin')
    print(f'### adjusted toast starting position: {randomstartoast}')

    ensemble(randomstartoaster1)