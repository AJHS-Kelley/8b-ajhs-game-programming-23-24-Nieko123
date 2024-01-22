# Number Slider, by Nieko Garnes, based project by Al Sweigart, v0.0

import sys, random, pygame
# sys module provides access to system resources (i.e. Operating system commands)

from pygame.locals import *
# Allows us to call functions form pygame using just the function name intead of module.function()
# Example: We can use draw() instead of pygame.draw()

# Constants for Game board
BOARDWIDTH = 4 #COLLUMS
BOARDHEIGHT = 4 # ROWS
TILESIZE = 80 # WHAT UNIT DO YOU THINK IS?
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
FPS = 30
BLANK = None

