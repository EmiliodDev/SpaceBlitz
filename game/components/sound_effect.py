import pygame as pg

class SoundEffect:
    def __init__(self, sound):
        self.sound_effect = sound
        self.sound_effect = pg.mixer.Sound(self.sound_effect)
        self.sound_effect.set_volume(0.2)

    def update(self):
        self.sound_effect.play()
