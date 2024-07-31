import pygame as pg
from math import degrees, atan2
from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet
from game.utils.constants import (
        SPACESHIP,
        SCREEN_WIDTH,
        SCREEN_HEIGHT,
        DEFAULT_SIZE_SHIP,
        SHIPS_MARGIN,
        DEFAULT_TYPE,
        SMALL_HEART
)


class Spaceship(Sprite):
    INITIAL_POSITION = ((SCREEN_WIDTH // 2) - DEFAULT_SIZE_SHIP[0], 500)
    SPEED = 5

    def __init__(self):
        super().__init__()
        self.image = SPACESHIP
        self.image = pg.transform.scale(self.image, DEFAULT_SIZE_SHIP)
        self.rect = self.image.get_rect(center=self.INITIAL_POSITION)
        self.speed = self.SPEED
        self.type = "player"
        self.power_up_type = DEFAULT_TYPE
        self.has_power_up = False
        self.time_with_power_up = 0
        self.coldown = 0  # coldown shooting
        self.lives = 3  # the player's lives

    def update(self, user_key_input, user_mouse_input, cursor, game):
        if self.coldown > 0:
            self.coldown -= 1  # coldown decreasing
        self.rotate(cursor)  # rotate the spaceship to follow the cursor
        controls_mapping = {
            pg.K_a: self.move_left,
            pg.K_d: self.move_right,
            pg.K_w: self.move_up,
            pg.K_s: self.move_down
        }
        for key, move_method in controls_mapping.items():
            if user_key_input[key]:
                move_method()
        if user_mouse_input[0]:  # use the click to shoot
            self.shoot(game.bullet_manager, cursor, game.player_sound)

    def rotate(self, position):  # get the updated cursor position
        dx = position[0] - self.rect.centerx
        dy = position[1] - self.rect.centery
        # calculates the angle to follow the cursor position
        angle = degrees(atan2(-dy, dx)) - 90

        # rotate the sprite to follow the cursor
        self.rotated_image = pg.transform.rotate(self.image, angle)
        self.rotated_rect = self.rotated_image.get_rect(
                center=self.rect.center
                )

    def set_image(self, image=SPACESHIP, size=DEFAULT_SIZE_SHIP):
        self.image = image
        self.image = pg.transform.scale(self.image, size)

    def move_left(self):
        self.rect.x -= self.speed
        if self.rect.left <= 0 - DEFAULT_SIZE_SHIP[0]:
            # gives a smoother visual effect
            self.rect.x = SCREEN_WIDTH - DEFAULT_SIZE_SHIP[0]//2

    def move_right(self):
        self.rect.x += self.speed
        if self.rect.right >= SCREEN_WIDTH + DEFAULT_SIZE_SHIP[0]:
            self.rect.x = 0 - DEFAULT_SIZE_SHIP[0]//2

    def move_up(self):
        if self.rect.y > 0:  # modified movement zone
            self.rect.y -= self.speed

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - SHIPS_MARGIN:
            self.rect.y += self.speed

    def draw(self, screen):
        # draw the rotated sprite
        self.draw_lives(screen)
        screen.blit(self.rotated_image, self.rect.center)

    def shoot(self, bullet_manager, target, sound_effect):
        if self.coldown == 0:
            bullet = Bullet(self, target)
            sound_effect.update()  # play the shoot sound effect
            bullet_manager.add_bullet(bullet)
            self.coldown += 10  # player can shoot every 10 iterations

    # resets the position of the player
    def reset(self):
        self.lives = 3
        self.image = pg.transform.scale(SPACESHIP, DEFAULT_SIZE_SHIP)
        self.rect = self.image.get_rect(center=self.INITIAL_POSITION)

    def draw_lives(self, screen):  # show the lives in the screen
        small_heart = pg.transform.scale(SMALL_HEART, (30, 30))
        position_x = 20
        for live in range(self.lives):
            position_x += 35
            screen.blit(small_heart, (position_x, 20))
