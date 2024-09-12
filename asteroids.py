import pygame
from constants import WHITE
from circleshape import CircleShape
class Asteroid(CircleShape):
	def __init__(self, x, y, radius, velocity):
		super().__init__(x,y,radius)
		self.velocity = velocity
	def draw(self, screen):
		pygame.draw.circle(screen, WHITE, (self.position.x, self.position.y), self.radius, 2)

	def update(self, dt):
		self.position.x += self.velocity.x * dt
		self.position.y += self.velocity.y * dt
