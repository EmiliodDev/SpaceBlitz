import pygame as pg
from random import randint
from game.components.power_ups.shield import Shield
from game.components.power_ups.live import Live
from game.utils.constants import SPACESHIP_SHIELD


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = randint(5000, 10000)  # time to appear
        self.duration = randint(3, 5)

    def update(self, game):
        current_time = pg.time.get_ticks()

        # Generate power ups
        if (len(self.power_ups) < 1
                and current_time >= self.when_appears):
            self.generate_power_up()

        # Update each power up
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            # Verify collision between player and powerUp
            if power_up.rect.colliderect(game.player.rotated_rect) and power_up.type == "shield":
                power_up.start_time = pg.time.get_ticks()
                game.player.power_up_type = power_up.type
                game.player.has_power_up = True
                game.player.time_with_power_up = power_up.start_time + self.duration * 1000
                # Change player ship
                game.player.set_image(SPACESHIP_SHIELD, (44, 44))
                self.power_ups.remove(power_up)
            elif power_up.rect.colliderect(game.player.rotated_rect):
                game.player.lives += 1
                self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def generate_power_up(self):
        if randint(1, 2) == 1:
            power_up = Shield()
        else:
            power_up = Live()
        self.power_ups.append(power_up)
        self.when_appears += randint(5000, 10000)

    def reset(self):
        self.power_ups = []
        now = pg.time.get_ticks()
        self.when_appears = randint(now + 5000, now + 10000)
        self.duration = randint(3, 5)
