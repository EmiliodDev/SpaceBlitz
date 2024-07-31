import pygame as pg
from game.components.game import Game

if __name__ == "__main__":
    game = Game()
    game.execute()
    pg.mixer.quit()
