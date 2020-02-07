#!/usr/bin/env python2

import pygame
from Field import Field
from Tiles import Tiles
from Frog import Frog
import random

WIDTH = 1280
HEIGHT = 720
FPS = 30

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

## initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("<Your game>")
clock = pygame.time.Clock()  ## For syncing the FPS

game = Field(Tiles(0))
frog = Frog(5, 1, game)


## Game loop
running = True
while running:

    # 1 Process input/events
    clock.tick(FPS)  ## will make the loop run at the same speed all the time
    for event in pygame.event.get():  # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    game.draw(0, screen)
    frog.draw(screen)

    ## Done after drawing everything to the screen
    pygame.display.flip()

pygame.quit()