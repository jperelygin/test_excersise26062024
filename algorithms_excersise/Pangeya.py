import random
from collections import deque
import config


class Pangeya:

    def __init__(self):
        self.field = []
        self.rows = 0
        self.colums = 0
        self.player = ()
        self.destination = ()
        self.path = []

    def __repr__(self) -> str:
        string = ""
        for i in self.field:
            string += str(i) + '\n'
        return string

    def generate_field(self, coord: tuple[int, int]) -> bool:
        if coord[0] < config.MINIMUM_FIELD_SIZE or coord[1] < config.MINIMUM_FIELD_SIZE:
            print(f"Field can't be smaller then {config.MINIMUM_FIELD_SIZE}x{config.MINIMUM_FIELD_SIZE}")
            return False
        for _ in range(0, coord[1]):
            self.field.append([random.choices(config.POSSIBLE_FIELDS, [config.WATER_WEIGHT, 1-config.WATER_WEIGHT])[0] for i in range(0,coord[0])])
        self.rows = coord[0]
        self.colums = coord[1]
        return True

    def is_water_check(self, coord: tuple[int, int]) -> bool:
        try:
            is_water = False
            if self.field[coord[0]][coord[1]] == config.WATER:
                is_water = True
            return is_water
        except IndexError:
            return False

    def _place_marker(self, coord: tuple[int, int], marker: str) -> bool:
        if self.is_water_check(coord):
            self.field[coord[0]][coord[1]] = marker
            return True
        else:
            print(f"Marker {marker} can not be placed at ({coord[0]}, {coord[1]}).")
            return False

    def place_player(self, coord: tuple[int, int]):
        self.player = (coord[0], coord[1])
        return self._place_marker(coord, config.PLAYER)

    def place_destination(self, coord: tuple[int, int]):
        self.destination = (coord[0], coord[1])
        return self._place_marker(coord, config.DESTINATION)

    def find_bfs_path(self):
        player_directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque([(self.player[0], self.player[1], [])])
        visited_cells = set()
        visited_cells.add(self.player)
        while queue:
            x, y, path = queue.popleft()
            if (x, y) == self.destination:
                self.path = path + [(x, y)]
                return
            for x_change, y_change in player_directions:
                new_x, new_y = x + x_change, y + y_change
                if 0 <= new_x < self.rows and 0 <= new_y < self.colums and (new_x, new_y) not in visited_cells:
                    if self.field[new_x][new_y] == config.WATER or self.field[new_x][new_y] == config.DESTINATION:
                        queue.append((new_x, new_y, path + [(x, y)]))
                        visited_cells.add((new_x, new_y))
        raise Exception("There is no possible path to destination.")

    def update_map_with_path(self):
        for i in self.path[1:-1]:
            self.field[i[0]][i[1]] = config.PATH
