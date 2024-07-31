import pygame as pg
from random import randint
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT


class PowerUp(pg.sprite.Sprite):
    def __init__(self, image, type):
        self.image = image
        self.image = pg.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = randint(120, SCREEN_WIDTH - 160)
        self.rect.y = 0
        self.type = type
        self.start_time = 0

    def update(self, game_speed, power_ups):
        self.rect.y += game_speed

        if self.rect.y < 0 or self.rect.y >= SCREEN_HEIGHT:
            power_ups.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
