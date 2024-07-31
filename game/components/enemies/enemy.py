import pygame as pg
from math import degrees, atan2
from random import randint
from game.components.bullets.bullet import Bullet
from game.utils.constants import (
        ENEMY_1,
        SCREEN_HEIGHT,
        SCREEN_WIDTH,
        DEFAULT_SIZE_SHIP
        )


class Enemy(pg.sprite.Sprite):
    X_POS_LIST = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550]
    Y_POS = 20
    SPEED_Y = 1
    SPEED_X = 3
    MOV_X = {0: "left", 1: "right"}

    def __init__(self):
        self.image = ENEMY_1
        self.image = pg.transform.scale(self.image, DEFAULT_SIZE_SHIP)
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS_LIST[randint(0, 10)]
        self.rect.y = self.Y_POS
        self.speed_y = self.SPEED_Y
        self.speed_x = self.SPEED_X
        self.movement_x = self.MOV_X[randint(0, 1)]
        self.index = 0
        self.move_x_for = randint(30, 100)
        self.type = "enemy"
        self.coldown = 0

    def update(self, ships, game):
        # decrease the coldown
        if self.coldown > 0:
            self.coldown -= 1

        self.rotate(game.player.rect.center)
        self.rect.y += self.speed_y
        self.shoot(game.bullet_manager, game.player.rect.center, game.enemy_sound)
        if self.movement_x == "left":
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x
        self.change_movement_x()

        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)

    def draw(self, screen):
        screen.blit(self.rotated_image, self.rotated_rect)

    def change_movement_x(self):
        self.index += 1

        if ((self.index >= self.move_x_for and self.movement_x == "right")
                or self.rect.x >= SCREEN_WIDTH - DEFAULT_SIZE_SHIP[0]):
            self.movement_x = "left"
            self.index = 0
        elif (self.index >= self.move_x_for and self.movement_x == "left") or self.rect.x <= 0:
            self.movement_x = "right"
            self.index = 0

    def shoot(self, bullet_manager, target, sound_effect):
        if self.coldown == 0:
            bullet = Bullet(self, target)
            sound_effect.update()
            bullet_manager.add_bullet(bullet)
            self.coldown = randint(50, 100)

    def rotate(self, position):  # get the updated player position
        dx = position[0] - self.rect.centerx
        dy = position[1] - self.rect.centery
        # calculates the angle to follow the player position
        angle = degrees(atan2(-dy, dx)) + 90

        # rotate the sprite to follow the player
        self.rotated_image = pg.transform.rotate(self.image, angle)
        self.rotated_rect = self.rotated_image.get_rect(
                center=self.rect.center
                )
