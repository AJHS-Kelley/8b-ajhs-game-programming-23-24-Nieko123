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
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Track')

sky_surface = pygame.image.load('img/ultPie/Sky.png').convert()
ground_surface = pygame.image.load('img/ultPie/trackground.png').convert()

difficulty = int(input("Please chose a difficulty, Enter 1 for Easy or 2 Hard.\n"))

if difficulty ==1:
   pygame.display.set_caption('Track -- EASY') 
else:
    pygame.display.set_caption('Track -- HARD')

screen.blit(background_surface,(400,400))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

		if game_active:
			if event.type == obstacle_timer:
				obstacle_group.add(Obstacle(choice(['','','',''])))
		
		else:
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				game_active = True
				start_time = int(pygame.time.get_ticks() / 1000)


	if game_active:
		screen.blit(sky_surface,(0,0))
		screen.blit(ground_surface,(0,300))
		score = display_score()
		
		player.draw(screen)
		player.update()

		obstacle_group.draw(screen)
		obstacle_group.update()

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
	clock.tick(60)


#Back Ground
# background_surface = pygame.image.load('img/ultPie/trackbackground.png').convert()

