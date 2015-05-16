from copy import deepcopy


with open("C:/Users/Maciek/PacMan/pacfunctions/lvl2.txt") as file:
    path_array = [[int(digit) for digit in list(line) if digit != '\n'] for line in file]
    path_array_copy = deepcopy(path_array)


def shortest_way(place_from, place_to, road_value=0):
    to_path_array()
    point_neighbours = neighbours(place_from)
    while place_to not in point_neighbours:
        road_value += 1
        increse(point_neighbours, road_value)
        point_neighbours = list(set([point for points in list(map(neighbours, point_neighbours)) for point in points]))

    return list(reversed(colect_way_back(place_to, road_value)))


def colect_way_back(place_to, road_value):
    road_back = []
    while road_value > 0:
        for point in road_neighbour(place_to):
            if path_array[point[0]][point[1]] == road_value:
                road_back.append(point)
                place_to = point
                road_value -= 1
                break
    return road_back


def increse(points, road_value):
    for point in points:
        path_array[point[0]][point[1]] = road_value


def road_neighbour(point):
    return [valid_point for valid_point in [(point[0], point[1] - 1), (point[0] - 1, point[1]),
                                            (point[0], point[1] + 1), (point[0] + 1, point[1])] if
            valid_coord(valid_point)]


def neighbours(point):
    return [valid_point for valid_point in [(point[0], point[1] - 1), (point[0] - 1, point[1]),
                                            (point[0], point[1] + 1), (point[0] + 1, point[1])] if valid(valid_point)]


def valid(point):
    return valid_coord(point) and valid_value(point)


def valid_coord(point):
    return 0 <= point[0] < len(path_array) \
           and 0 <= point[1] < len(path_array[0])


def valid_value(point):
    return path_array[point[0]][point[1]] == 0


def to_path_array():

    for y in range(len(path_array)):
        for x in range(len(path_array[0])):
            if path_array_copy[y][x] != 0:
                path_array[y][x] = '*'
            else:
                path_array[y][x] = 0

