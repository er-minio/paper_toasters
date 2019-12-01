from test_functions import *
import os, sys
import pygame
from pygame.locals import *
if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')
import random
from PIL import Image, ImageDraw, ImageFont
from IT8951 import constants
from sys import path
path += ['../../']
from IT8951.display import AutoEPDDisplay

def screeninit():
    print('Initializing EPD...')
    display = AutoEPDDisplay(vcom=-2.06)
    print('VCOM set to', display.epd.get_vcom())
    # clearing image to black
    display.frame_buf.paste(0x00, box=(0, 0, display.width, display.height))
    print('Clearing screen to black')
    # TODO: this should be built-in
    dims = (display.width, display.height)

SIZE = WIDTH, HEIGHT = 800, 600 #the width and height of our screen
BACKGROUND_COLOR = pygame.Color('black') #The background colod of our window
FPS = 10 #Frames per second
 
class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()
 
        self.images = []
        self.images.append(pygame.image.load('sprite/toaster_01.png'))
        self.images.append(pygame.image.load('sprite/toaster_02.png'))
        self.images.append(pygame.image.load('sprite/toaster_03.png'))
        self.images.append(pygame.image.load('sprite/toaster_04.png'))

        self.index = 0
 
        self.image = self.images[self.index]
 
        self.rect = pygame.Rect(5, 5, 150, 198)
 
    def update(self):
        self.index += 1
 
        if self.index >= len(self.images):
            self.index = 0
        
        self.image = self.images[self.index]
 
def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    my_sprite = MySprite()
    my_group = pygame.sprite.Group(my_sprite)
    clock = pygame.time.Clock()
 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 
        my_group.update()
        screen.fill(BACKGROUND_COLOR)
        my_group.draw(screen)
        pygame.display.update()
        clock.tick(10)
        paste_coords = 0, 0
        display.frame_buf.paste(screen, paste_coords)
        display.draw_partial(constants.DisplayModes.DU)
 
if __name__ == '__main__':
    screeninit()
    main()