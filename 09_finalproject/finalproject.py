# Final Project, Nieko Garnes, v0.0
import sys, random, pygame

resolution = 0 #0 = Low resolution (800, 600),1 = High Resilution (1920, 1080)

if resolution == 0:
    x = 800
    y = 600
else:
    x = 1920
    y = 1080

pygame.init()

difficulty = int(input("Please chose a difficulty, Enter 1 for Easy or 2 Hard.\n"))

if difficulty ==1:
   pygame.display.set_caption('NAME OF GAME -- EASY') 
else:
    pygame.display.set_caption('NAME OF GAME -- HARD')

screen = pygame.display.set_mode((x, y))
