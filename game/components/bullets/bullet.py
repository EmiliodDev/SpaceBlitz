import pygame as pg
from math import degrees, atan2
from game.utils.constants import (
        BULLET,
        BULLET_ENEMY,
        SCREEN_HEIGHT,
        SCREEN_WIDTH
        )


class Bullet(pg.sprite.Sprite):
    BULLET_SIZE = pg.transform.scale(BULLET, (10, 20))
    BULLET_ENEMY_SIZE = pg.transform.scale(BULLET_ENEMY, (9, 32))
    BULLETS = {"player": BULLET_SIZE, "enemy": BULLET_ENEMY_SIZE}
    DEFAULT_SPEED = 7
    PLAYER_SPEED = 10

    def __init__(self, spaceship, target):
        self.image = self.BULLETS[spaceship.type]
        self.rect = self.image.get_rect()
        self.rect.center = spaceship.rect.center
        self.owner = spaceship.type
        self.speed = self.DEFAULT_SPEED
        self.target = target

    # rotates the bullet in the direction of its target
    def rotate_bullet(self):
        speed = self.speed
        dx = self.target[0] - self.rect.x
        dy = self.target[1] - self.rect.y
        angle = degrees(atan2(-dy, dx)) - 90

        self.rotated_image = pg.transform.rotate(self.image, angle)
        self.rotated_rect = self.rotated_image.get_rect(center=self.rect.center)

        # calculates the vector to follow
        direction = pg.math.Vector2(
                self.target[0] - self.rotated_rect.x,
                self.target[1] - self.rotated_rect.y
                )
        if self.owner == "player":
            speed = self.PLAYER_SPEED

        self.velocity = direction.normalize() * speed

    def update(self, bullets, target):
        # bullet follows the vector
        self.rotated_rect.move_ip(self.velocity)
        # verify if the bullet leave the screen and delete it
        if ((self.rotated_rect.y >= SCREEN_HEIGHT
            or self.rotated_rect.y <= 0)
                or (self.rotated_rect.x >= SCREEN_WIDTH
                    or self.rotated_rect.x <= 0)):
            bullets.remove(self)

    def draw(self, screen):
        screen.blit(self.rotated_image, self.rotated_rect.center)
