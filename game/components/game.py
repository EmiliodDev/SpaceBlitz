import pygame as pg
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_manager import EnemyManager
from game.components.cursor import Cursor
from game.components.menu import Menu
from game.components.counter import Counter
from game.components.sound_effect import SoundEffect
from game.components.power_ups.power_up_manager import PowerUpManager
from game.components.bullets.bullet_manager import BulletManager
from game.utils.constants import (
        BG,
        ICON,
        SCREEN_HEIGHT,
        SCREEN_WIDTH,
        TITLE,
        FPS,
        FONT_STYLE,
        DEFAULT_TYPE,
        SMALL_SHIELD,
        SOUNDTRACK,
        PLAYER_GUN,
        ENEMY_GUN,
        GAME_OVER
        )

class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption(TITLE)
        pg.display.set_icon(ICON)
        pg.mixer.music.load(SOUNDTRACK)  # loads the soundtrack music
        pg.mixer.music.set_volume(0.7)
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pg.time.Clock()
        self.playing = False
        self.game_speed = 2
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.user_cursor = Cursor()
        self.bullet_manager = BulletManager()
        self.menu = Menu(self.screen)
        self.running = False
        self.death_count = Counter()
        self.score = Counter()
        self.highest_score = Counter()
        self.power_up_manager = PowerUpManager()
        self.player_sound = SoundEffect(PLAYER_GUN)
        self.enemy_sound = SoundEffect(ENEMY_GUN)
        self.gameover_sound = SoundEffect(GAME_OVER)

    def show_menu(self):
        icon = pg.transform.scale(ICON, (80, 80))
        half_screen_icon = (SCREEN_WIDTH // 2 - 40, SCREEN_HEIGHT // 2 - 120)
        # show the spaceship in the menu
        self.screen.blit(icon, (half_screen_icon))
        # show the menu
        if self.death_count.count == 0:
            self.menu.draw(self.screen, "Press Enter to start...")
        else:  # when the player dies, show the scores in menu
            self.update_highest_score()
            self.menu.draw(self.screen, "GAME OVER. Press Enter to start...")
            self.menu.draw(self.screen, f"Score: {self.score.count}", SCREEN_WIDTH // 2, 350)
            self.menu.draw(self.screen, f"Highest score: {self.highest_score.count}", SCREEN_WIDTH // 2, 400)
            self.menu.draw(self.screen, f"Total deaths: {self.death_count.count}", SCREEN_WIDTH // 2, 450)

        self.menu.update(self)

    def execute(self):
        # show the menu before the game starts
        self.running = True

        while self.running:
            if not self.playing:
                self.draw_background()  # draw the background in-menu
                self.show_menu()
        pg.display.quit()
        pg.quit()

    def run(self):
        # resets the game
        self.resets()
        # Game loop: events - update - draw
        pg.mouse.set_visible(False)
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        self.gameover_sound.update()  # plays the gameover sound effect
        pg.mixer.music.stop()  # stops the soundtrack in the menu

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False

    def update(self):
        user_key_input = pg.key.get_pressed()
        user_mouse_input = pg.mouse.get_pressed()
        self.user_cursor.update()  # updating the mouse coordenates
        # passing the updated coordenates
        self.player.update(
                user_key_input,
                user_mouse_input,
                self.user_cursor.rect.center,
                self
                )
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)
        self.power_up_manager.update(self)

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.score.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        self.user_cursor.draw(self.screen)  # draw the pointer
        # update() eliminated
        pg.display.flip()  # update full display surface to the screen.

    def draw_background(self):
        image = pg.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()

        self.y_pos_bg += self.game_speed

        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))

        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (
                self.x_pos_bg,
                self.y_pos_bg - image_height)
                )
            self.y_pos_bg = 0

    def update_highest_score(self):
        if self.score.count > self.highest_score.count:
            self.highest_score.set_count(self.score.count)

    def resets(self):  # resets all parameters
        self.score.reset()
        self.enemy_manager.reset()
        self.bullet_manager.reset()
        self.player.reset()
        self.power_up_manager.reset()
        pg.mixer.music.play(-1)  # play the soundtrack

    def draw_power_up_time(self):  # show the shield duration
        if self.player.has_power_up:
            shield_icon = pg.transform.scale(SMALL_SHIELD, (30, 30))
            time_to_show = round((self.player.time_with_power_up - pg.time.get_ticks()) / 1000, 0)
            if time_to_show > 0:
                self.screen.blit(shield_icon, (500, 20))
                self.menu.draw(self.screen, f"{time_to_show}'s", 580, 35)
            else:
                self.player.has_power_up = False
                self.player.power_up_type = DEFAULT_TYPE
                self.player.set_image()
