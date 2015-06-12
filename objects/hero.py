from pygame.constants import *
from pygame.rect import Rect
from events.eventobserver import EventObserver

class Hero(EventObserver):

    def __init__(self, x, y, rect_martix, container, evenent_handler):
        super().__init__(container, evenent_handler)
        self.rect_matrix = rect_martix
        self.map_point = (y, x) #cooridnates on map.txt
        self.x = x * 20 - 3 # coordinates used to paint object
        self.y = y * 20 - 3
        self.speed = 2
        self.active = True
        self.area_rect = Rect(self.x + 3, self.y + 3, 20, 20)
        self.direction = K_RIGHT
        self.new_direction = K_RIGHT
        self.movements = {K_UP: (0, -self.speed), K_RIGHT: (self.speed, 0),
                          K_DOWN: (0, self.speed), K_LEFT: (-self.speed, 0),
                          K_DELETE : (0, 0)}

    def move_hero(self, arguments):
        pass

    def move(self):
        self.x += self.movements[self.direction][0]
        self.y += self.movements[self.direction][1]
        self.area_rect.move_ip(self.movements[self.direction][0], self.movements[self.direction][1])

    def go_back(self):
        self.x -= self.movements[self.direction][0]
        self.y -= self.movements[self.direction][1]
        self.area_rect.move_ip(-self.movements[self.direction][0], -self.movements[self.direction][1])

    def get_proper_random_direction(self):
        if not self.is_this_the_wall(K_UP):
            return K_UP
        elif not self.is_this_the_wall(K_RIGHT):
            return K_RIGHT
        elif not self.is_this_the_wall(K_DOWN):
            return K_DOWN
        elif not self.is_this_the_wall(K_LEFT):
            return K_LEFT

    def in_place_to_change_direction(self):
        return self.rect_matrix.is_at_direction_change_place(self.area_rect)

    #checks if next point with givien direction to current hero map_point have wall on it
    def is_this_the_wall(self, direction):
         return self.rect_matrix.is_this_the_wall(self.area_rect, (int(self.movements[direction][0]/self.speed),
                                                             int(self.movements[direction][1]/self.speed)))

    def reload_movements(self):
        self.movements = {K_UP: (0, -self.speed), K_RIGHT: (self.speed, 0),
                          K_DOWN: (0, self.speed), K_LEFT: (-self.speed, 0),
                          K_DELETE: (0, 0)}

    def teleport(self, map_point):
        self.map_point = map_point #cooridnates on map.txt
        self.x = map_point[1] * 20 - 3 # coordinates used to paint object
        self.y = map_point[0] * 20 - 3
        self.area_rect = Rect(self.x + 3, self.y + 3, 20, 20)





