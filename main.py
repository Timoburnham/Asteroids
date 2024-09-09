# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, PLAYER_TURN_SPEED
from player import Player

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2, 30)
	running = True	
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		screen.fill(BLACK)
		player.draw(screen)
		player.update(dt)
		pygame.display.flip()
		dt = clock.tick(60) / 1000.0
if __name__ == "__main__":
    main()

