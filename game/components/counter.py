import pygame as pg
from game.utils.constants import FONT_STYLE

class Counter:
    def __init__(self):
        self.count = 0

    def update(self):
        self.count += 1

    def set_count(self, value):
        self.count = value

    def draw(self, screen):
        font = pg.font.Font(FONT_STYLE, 30)
        text = font.render(
                f"Score: {self.count}",
                True,
                (255, 255, 255))
        text_rect = text.get_rect(center=(1000, 30))
        screen.blit(text, text_rect)

    def reset(self):
        self.count = 0
