from copy import deepcopy
import sys

import pygame
from pygame.locals import *

from media.dirtyrect import add_dirty_rect
import media.sprites
from objects.Container import get_ghosts
from objects.hero import Hero, RECT_MATRIX
from game_engine.gameengine import BG_MATRIX
from media.dirtyrect import PacDirtyRect
from pacfunctions.pacfunction import next_point_in_direction

class PacMan(Hero):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.animations = media.sprites.PacManAnim
        self.react_cases = {"DEATH": self.die}
        self.alive = True
        self.is_dot = False
        self.lives_left = 3
        for key, animation in self.animations.items():
            animation.play()

    def move(self):
        super().move()
       # add_dirty_rect(PacDirtyRect(Rect(self.x - 2, self.y - 2, 30, 30), self.is_dot))

    def move_hero(self, arguments):
        key_events = arguments[0]
        for event in key_events:
            if event.type == KEYDOWN:
                self.new_direction = event.key #jesli klawisz wcisniety to pobierz kierunek do zmian
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()
        if self.in_place_to_change_direction():
            self.map_point = RECT_MATRIX.get_map_point(self.area_rect)# na podstawie swojego rect znajdz wspolrzedne mapowe
            self.eat_dot()
            if not self.is_this_the_wall(self.new_direction):
                self.direction = self.new_direction #zmie? kierunek tylko gdy nowy nie jest w kierunku sciany

            if self.is_this_the_wall(self.direction):
                self.go_back() #jesli o pole w obecnym kierunku mamy sciane to cofnij sie
        self.move()

    def eat_dot(self):
        RECT_MATRIX.eat_dot(self.map_point)

    def predicted_pac_man_point(self, steps_to_predict):
        pac_point = self.map_point
        pac_direction = deepcopy(self.direction)
        while steps_to_predict > 0:

            if not RECT_MATRIX.is_wall_at_field(next_point_in_direction(pac_point, pac_direction)):
                pac_point = next_point_in_direction(pac_point, pac_direction)
            else:
                pac_direction = RECT_MATRIX.get_proper_random_direction(pac_point, pac_direction)
                pac_point = next_point_in_direction(pac_point, pac_direction)
            steps_to_predict -= 1
        return pac_point

    def die(self):
        #for key, val in self.animations.items():
        #    val.rewind()
        #    val.play()
        self.direction = K_DELETE
        self.active = False
        #self.animations = media.sprites.DeathAnim

