from pygame import *
import pygame as pg
from gamesettings import *
vec = pg.math.Vector2

import os

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"image")

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(img_folder,"哪吒.gif"))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (WINDOW_WIDTH / 2,WINDOW_HEIGHT)
        self.pos = vec(WINDOW_WIDTH / 2,WINDOW_HEIGHT)
        self.vel = vec(0,0)
        self.acc = vec(0,0)


    def update(self):
        self.acc = vec(0,0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        self.acc.x += self.vel.x * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > WINDOW_WIDTH + self.rect.width / 2:  # wholly enter
            self.pos.x = 0 - self.rect.width / 2
        if self.pos.x < 0 - self.rect.width / 2:
            self.pos.x =WINDOW_WIDTH + -self.rect.width / 2

        self.rect.midbottom = self.pos










