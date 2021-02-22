import pygame
from pygame.locals import *

pygame.init()

# Game loop begins
while True:
    # code
    # code
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()