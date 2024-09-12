# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, PLAYER_TURN_SPEED
from player import Player
from asteroidfield import AsteroidField
from asteroids import Asteroid

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	updateable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	Player.containers = (updateable, drawable)
	Asteroid.containers = (asteroids, updateable, drawable)
	AsteroidField.containers = (updateable,)
	asteroid_field = AsteroidField()
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2, 30)
	running = True	
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		screen.fill(BLACK)
		for sprite in drawable:
			sprite.draw(screen)
		updateable.update(dt)
		pygame.display.flip()
		dt = clock.tick(60) / 1000.0

		for asteroid in asteroids:
			if player.collide(asteroid):
				print("Game over!")
				sys.exit()
if __name__ == "__main__":
    main()
