import random
from PIL import Image, ImageDraw, ImageFont
from IT8951 import constants
from sys import path
path += ['../../']
from IT8951.display import AutoEPDDisplay

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

def toaster_anim():
    while True:
        hor1 = random.randint(1,800)
        ver = random.randint(-100,0)
        while hor1 > -164: # or ver > 974:
            print(f'toaster {hor1}, {ver}')    
            img1 = Image.open(img1_path)
            paste_coords = hor1, ver
            display.frame_buf.paste(img1, paste_coords)
            display.draw_partial(constants.DisplayModes.DU)
            hor1 = hor1 - shift
            ver = ver + shift
            
            img2.thumbnail(dims)
            paste_coords = hor1, ver
            display.frame_buf.paste(img2, paste_coords)
            display.draw_partial(constants.DisplayModes.DU)
            hor1 = hor1 - shift
            ver = ver + shift
            
            img3.thumbnail(dims)
            paste_coords = hor1, ver
            display.frame_buf.paste(img3, paste_coords)
            display.draw_partial(constants.DisplayModes.DU)
            hor1 = hor1 - shift
            ver = ver + shift
            
            img4.thumbnail(dims)
            paste_coords = hor1, ver
            display.frame_buf.paste(img4, paste_coords)
            display.draw_partial(constants.DisplayModes.DU)
            hor1 = hor1 - shift
            ver = ver + shift
            
            img3.thumbnail(dims)
            paste_coords = hor1, ver
            display.frame_buf.paste(img3, paste_coords)
            display.draw_partial(constants.DisplayModes.DU)
            hor1 = hor1 - shift
            ver = ver + shift
            
            img2.thumbnail(dims)
            paste_coords = hor1, ver
            display.frame_buf.paste(img2, paste_coords)
            display.draw_partial(constants.DisplayModes.DU)
            hor1 = hor1 - shift
            ver = ver + shift
            
            print('toaster off screen / reset')
            
def toast_anim():
    while True:
        hor2 = random.randint(1,800)
        ver2 = random.randint(-100,0)
        while hor1 > -164:
            #toast
            print(f'toast {hor1}, {ver}')
            toast.thumbnail(dims)
            paste_coords = hor2, ver2
            display.frame_buf.paste(toast, paste_coords)
            display.draw_partial(constants.DisplayModes.DU)
        
            hor2 = hor2 - shift
            ver2 = ver2 + shift
            
            print('toast off screen / reset')
            
def flock():
    while True:
        # toaster_anim()
        toast_anim()
            
        
def ensemble(randomstart):
    start1 = randomstartoaster1
    start2 = randomstartoaster2
    start3 = randomstartoast
    hor1 = start1
    hor2 = start2
    hor3 = start3
    versource = random.randint(164,200)
    ver = -versource
    horizontal_stop = -200
    while hor3 >= horizontal_stop:
    
        img1 = Image.open(img1_path)
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
w_start = 200
w_stop = 1000
while True:
    
    #randomizing start point and detecting collisions
    randomstartoaster1 = random.randint(w_start,w_stop)
    print(f'### toaster1 starting position: {randomstartoaster1}')
    randomstartoaster2 = random.randint(w_start,w_stop)
    print(f'### toaster2 starting position: {randomstartoaster2}')
    randomstartoast = random.randint(w_start,w_stop)
    print(f'### toast starting position: {randomstartoast}')
    toastdelta = random.randint(164,300)
    print(f'### toast delta: {toastdelta}')
    delta = random.randint(164,450)
    print(f'### toaster delta: {delta}')
    
    #ranges
    toaster1_range = range(randomstartoaster1-164, randomstartoaster1+164)
    toaster2_range = range(randomstartoaster2-164, randomstartoaster2+164)
    toast_range = range(randomstartoast-164, randomstartoast+164)
    print(f'{toaster2_range}')
    
    #Toaster2 Overlap Check
    while randomstartoaster2 in toaster1_range:
     print(f'### toaster2 on toaster1 collision: {randomstartoaster2} #############################################')
     randomstartoaster2 = random.randint(w_start,w_stop)
     print('regenerating toaster2 origin')
    while randomstartoaster2 in toast_range:
     print(f'### toaster2 on toast collision: {randomstartoaster2} #############################################')
     randomstartoaster2 = random.randint(w_start,w_stop)
    print(f'### adjusted toaster2 starting position: {randomstartoaster2}')
    
    #Toast Overlap Check
    while randomstartoast in toaster1_range:
     print(f'### toast on toaster1 collision: {randomstartoast} #############################################')
     randomstartoast = random.randint(w_start,w_stop)
     print('regenerating toast origin')
    while randomstartoast in toaster2_range:
     print(f'### toast on toaster2 collision: {randomstartoast} #############################################')
     randomstartoast = random.randint(w_start,w_stop)
    print(f'### adjusted toast starting position: {randomstartoast}')

    # ensemble(randomstartoaster1)
    flock()