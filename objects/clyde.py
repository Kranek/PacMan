from objects.Container import get_object
from objects.hero import RECT_MATRIX
from pacfunctions.pacfunction import get_next_directions
import media
from objects.ghost import Ghost


class Clyde(Ghost):
    def __init__(self, x, y):
        super().__init__(x, y, media.sprites.ClydeAnim)
        self.house_time = 750
        self.corner_points = [(27, 1), (27, 12), (24, 12), (24, 6)]

    def chase_move(self): #sprawa z argumentami do przemyslenia
        if self.in_place_to_change_direction():
            self.map_point = RECT_MATRIX.get_map_point(self.area_rect)
            self.is_dot = self.is_dot_at_field()
            if self.change_direction_counter % self.stupidity == 0:
                self.change_direction_counter = 1
                self.new_directions = self.get_directions()
                self.direction = self.new_directions[0]
            else:
                if self.change_direction_counter < len(self.new_directions):
                    self.direction = self.new_directions[self.change_direction_counter]
                else:
                    self.direction = self.get_proper_random_direction()
                self.change_direction_counter += 1

    def get_directions(self):
        directions_to_pacman = get_next_directions(self.map_point, get_object(0).map_point)
        directions_to_left_corner = get_next_directions(self.map_point, (27, 1))
        if len(directions_to_pacman) <= 8:
            self.stupidity = len(directions_to_left_corner)
            return directions_to_left_corner
        else:
            self.stupidity = 6
            return directions_to_pacman
