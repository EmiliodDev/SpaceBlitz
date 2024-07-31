import pygame as pg
from game.utils.constants import (
        FONT_STYLE,
        SCREEN_WIDTH,
        SCREEN_HEIGHT
        )


class Menu:
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2

    def __init__(self, screen):
        screen.fill((0, 0, 0))
        self.font = pg.font.Font(FONT_STYLE, 30)

    def update(self, game):
        pg.display.update()
        self.handle_events_on_menu(game)

    def draw(self, screen, message, x=HALF_SCREEN_WIDTH, y=HALF_SCREEN_HEIGHT, color=(255, 255, 255)):
        text = self.font.render(message, True, color)
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)

    def handle_events_on_menu(self, game):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game.playing = False
                game.running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:  # Enter to start
                    game.run()
