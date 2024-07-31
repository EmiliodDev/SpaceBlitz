import pygame as pg
from random import randint
from game.utils.constants import ENEMY_2, SCREEN_HEIGHT, DEFAULT_SIZE_SHIP
from game.components.enemies.enemy import Enemy


class Assault(Enemy):
    ASLT_X_POS_LIST = [600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050]
    ASLT_SPEED = 3

    def __init__(self):
        super().__init__()
        self.image = ENEMY_2
        self.image = pg.transform.scale(self.image, DEFAULT_SIZE_SHIP)
        self.rect.x = self.ASLT_X_POS_LIST[randint(0, 9)]
        self.speed_x = self.ASLT_SPEED
        self.speed_y = self.ASLT_SPEED

    def update(self, ships, game):
        self.rotate(game.player.rect.center)
        self.shoot(game.bullet_manager, game.user_cursor.rect.center, game.enemy_sound)
        self.index += 1

        if self.index >= 30 and self.index <= 70:
            self.rect.y += self.speed_y
        elif self.index >= 70:
            self.index = 0

        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)

    def draw(self, screen):  # using draw method of Enemey
        return super().draw(screen)

    def shoot(self, bullet_manager, target, sound_effect):  # using shoot method of Enemy
        return super().shoot(bullet_manager, target, sound_effect)

    def rotate(self, position):  # re-using the rotate method of Enemy
        return super().rotate(position)
