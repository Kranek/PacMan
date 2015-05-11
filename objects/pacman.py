import media.sprites
from media.dirtyrect import *
from game_engine.game_engine import *


class PacMan:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 4
        self.animations = media.sprites.PacManAnim
        self.direction = K_RIGHT
        self.new_direction = K_RIGHT
        self.movements = {K_UP: (0, -self.speed), K_RIGHT: (self.speed, 0),
                          K_DOWN: (0, self.speed), K_LEFT: (-self.speed, 0), K_PAUSE: (0, 0)}

        for key, animation in self.animations.items():
            animation.play()

    def move(self, d_move):
        add_dirty_rect(Rect(self.x - self.speed, self.y - self.speed, 40, 40))
        self.x += d_move[0]
        self.y += d_move[1]
