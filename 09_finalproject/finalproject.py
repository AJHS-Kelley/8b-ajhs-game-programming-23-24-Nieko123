# Final Project, Nieko Garnes, v0.0
import sys, random, pygame


# test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

# game_name = test_font.render('Track game', False, (111, 196, 169))
# game_name_rect = game_name.get_rect(center = (400, 80))

# game_message = test_font.render('press Space to start', False, (111, 196, 169))
# game_name_rect = game_message.get_rect(center = (400, 330))

resolution = 0 #0 = Low resolution (800, 600),1 = High Resilution (1920, 1080)

if resolution == 0:
    x = 800
    y = 600
else:
    x = 1920
    y = 1080

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Track')

difficulty = int(input("Please chose a difficulty, Enter 1 for Easy or 2 Hard.\n"))

# sky_surface = pygame.image.load('img/ultPie/sponge_sky.jpg').convert()
ground_surface = pygame.image.load('img/ultPie/ground.png').convert()

# Intro screen
player_stand = pygame.image.load('img/ultPie/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200))

game_name = test_font.render('Pixel Runner',False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400,80))

game_message = test_font.render('Press space to run',False,(111,196,169))
game_message_rect = game_message.get_rect(center = (400,330))

# Timer 
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

		if game_active:
			screen.blit(ground_surface,(0,300))

		if event.type == obstacle_timer:
			pass
				# obstacle_group.add(Obstacle(choice(['fly','snail','snail','snail'])))
		else:
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				game_active = True
				start_time = int(pygame.time.get_ticks() / 1000)


	if game_active:
		# screen.blit(sky_surface,(0,0))
		screen.blit(ground_surface,(0,300))
		# score = display_score()
		
		# player.draw(screen)
		# player.update()

		# obstacle_group.draw(screen)
		# obstacle_group.update()

		game_active = collision_sprite()
		
	else:
		screen.fill((94,129,162))
		screen.blit(player_stand,player_stand_rect)

		score_message = test_font.render(f'Your score: {score}',False,(111,196,169))
		score_message_rect = score_message.get_rect(center = (400,330))
		screen.blit(game_name,game_name_rect)

		if score == 0: screen.blit(game_message,game_message_rect)
		else: screen.blit(score_message,score_message_rect)

	pygame.display.update()
	# clock.tick(60)


#Back Ground
background_surface = pygame.image.load('img/ultPie/trackbackground.png').convert()

