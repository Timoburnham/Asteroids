import pygame
from constants import WHITE, SHOT_RADIUS, PLAYER_SHOOT_SPEED
from circleshape import CircleShape
class Shot(CircleShape):
        def __init__(self, x, y, velocity):
                super().__init__(x,y, SHOT_RADIUS)
                self.velocity = velocity
        def draw(self, screen):
                pygame.draw.circle(screen, WHITE, (self.position.x, self.position.y), self.radius, 2)

        def update(self, dt):
                self.position.x += self.velocity.x * dt
                self.position.y += self.velocity.y * dt
