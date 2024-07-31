import pygame as pg
from game.utils.constants import CURSOR

class Cursor:
    def __init__(self):
        self.image = CURSOR
        self.image = pg.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)

    def update(self):
        self.rect.center = pg.mouse.get_pos()

    def draw(self, screen):
        screen.blit(self.image, self.rect.center)
