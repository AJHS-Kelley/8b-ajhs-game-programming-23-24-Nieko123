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

# COLOR VALUES IN (R, G, B) format.
# 0 = No values 255 = max values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BRIGHTBLUE = (0, 50, 255)
DARKTURQUOISE = (3, 54, 73)
GREEN = (0, 204, 0)

#BOARD DESIGN SETUP
BGCOLOR = DARKTURQUOISE
TILECOLOR = GREEN
TEXTCOLOR = WHITE
BOARDCOLOR = BRIGHTBLUE
BASICFONTSIZE = 20

#BUTTON SETUP
BUTTONCOLOR = WHITE
BUTTONTEXTCOLOR = BLACK
MASSAGECOLOR = WHITE

# ESTABLISH WINDOW MARGINS
XMARGIN = int((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)
# int((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (3))) / 2)
# int(((320 + (3))) / 2)
# int(((323 / 2)) / 2)
# int((640 - ())) / 2)
# int((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)

print(XMARGIN)
YMARGIN =