import pygame as pg
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 60
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
# sound effects
SOUNDTRACK = os.path.join(IMG_DIR, "sounds/soundtrack.mp3")
ENEMY_GUN = os.path.join(IMG_DIR, "sounds/laser.mp3")
PLAYER_GUN = os.path.join(IMG_DIR, "sounds/player_shoot.mp3")
GAME_OVER = os.path.join(IMG_DIR, "sounds/gameover_loud.mp3")

ICON = pg.image.load(os.path.join(IMG_DIR, "Spaceship/main_ship_1.png"))

SHIELD = pg.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pg.image.load(os.path.join(IMG_DIR, 'Other/PurpleBackground.png'))
# custom cursor
CURSOR = pg.image.load(os.path.join(IMG_DIR, 'Other/cursor.png'))

HEART = pg.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))
SMALL_HEART = pg.image.load(os.path.join(IMG_DIR, 'Other/heart.png'))  # sprite to show player's lives

# sprite to show the shield duration
SMALL_SHIELD = pg.image.load(os.path.join(IMG_DIR, "Other/small_shield.png"))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
HEART_TYPE = 'heart'

DEFAULT_SIZE_SHIP = (40, 40)  # default size for all regular spaceships
# constant distance for all spaceships, TOP & BOT screen edges
SHIPS_MARGIN = 70

SPACESHIP = pg.image.load(os.path.join(IMG_DIR, "Spaceship/main_ship_1.png"))
SPACESHIP_SHIELD = pg.image.load(os.path.join(IMG_DIR, "Spaceship/shield.png"))
BULLET = pg.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pg.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pg.image.load(os.path.join(IMG_DIR, "Enemy/enemy_ship.png"))
ENEMY_2 = pg.image.load(os.path.join(IMG_DIR, "Enemy/bomber_ship.png"))

FONT_STYLE = 'freesansbold.ttf'
