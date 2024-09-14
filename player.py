import pygame
from circleshape import CircleShape
from constants import PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS, PLAYER_SHOOT_COOLDOWN
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.shoot_timer = 0
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt, direction=1):
        self.rotation += PLAYER_TURN_SPEED * dt * direction
        self.rotation %= 360

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt, direction=-1)
        if keys[pygame.K_d]:
            self.rotate(dt, direction=1)
        if keys[pygame.K_w]:
            self.move(dt, direction =1)
        if keys[pygame.K_s]:
            self.move(dt, direction = -1)
        self.shoot_timer -= dt
        if self.shoot_timer < 0:
            self.shoot_timer = 0

    def move(self, dt, direction =1):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt * direction

    def shoot(self):
        if self.shoot_timer > 0:
            return None
        velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        new_shot = Shot(self.position.x, self.position.y, velocity)
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        return new_shot
