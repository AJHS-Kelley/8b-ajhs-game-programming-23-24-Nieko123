#Ultimate Pygame, Nieko Garnes
# Get it finished, almost done! 

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

sky_surf = pygame.image.load(('img/ultPie/sky.jpg')).convert()
ground_surf = pygame.image.load('img/ultPie/ground.jpg').convert()

score_surf = test_font.render('My game', False, (64,64,64))
score_rect = score_surf.get_rect(center = (400, 50))

snail_surf = pygame.image.load('img/ultPie/snail.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (80,300))

player_surf = pygame.image.load('img/ultPie/player_walk.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom =(0,0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTTON:
        #     if player_rect.collidepoint(event.pos): print('collision')

    screen.blit(sky_surf,(300,50))
    screen.blit(ground_surf,(0,300))
    pygame.draw.rect(screen,'Pink', score_rect)
    pygame.draw.rect(screen,'Pink', score_rect,10)
    screen.blit(score_surf,score_rect)

    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800
    screen.blit(snail_surf,snail_rect)
    screen.blit(player_surf,snail_rect)
    pygame.display.update()
    clock.tick(60)
