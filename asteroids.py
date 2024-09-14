import pygame
import random
from constants import WHITE, ASTEROID_MIN_RADIUS
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

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return []
		rand_angle = random.uniform(20, 50)
		new_vector_1 = self.velocity.rotate(rand_angle)
		new_vector_2 = self.velocity.rotate(-rand_angle)
		new_radius = self.radius - ASTEROID_MIN_RADIUS
		scaled_vector_1 = new_vector_1 * 1.2
		scaled_vector_2 = new_vector_2 * 1.2

		new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius, scaled_vector_1)
		new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius, scaled_vector_2)
		
		return [new_asteroid_1, new_asteroid_2]
