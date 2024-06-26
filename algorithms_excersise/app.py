from Pangeya import Pangeya


def get_input(object_name: str) -> tuple:
    result = input(f"Please enter {object_name} as 2 integers devided by comma:\n")
    try:
        result = tuple(int(i) for i in result.split(','))
        return result
    except ValueError:
        raise ValueError(f"Error! {object_name.capitalize()} should be only 2 integers separated by comma!")
    
def init_step(object_name: str, func):
    next_step = False
    while not next_step:
        int_tuple = get_input(object_name)
        next_step = func(int_tuple)

def game():
    print("Finding a shortest path from player to destination.")
    pangeya = Pangeya()
    init_step("field size", pangeya.generate_field)
    print(pangeya)
    init_step("start coordinates for player", pangeya.place_player)
    init_step("destination coordinates", pangeya.place_destination)
    print(pangeya)
    print("Finding closest path from player to destination")
    pangeya.find_bfs_path()
    path_string = ' -> '.join([f'({x}, {y})' for x, y in pangeya.path])
    print(f"Path is: {path_string}")
    pangeya.update_map_with_path()
    print(pangeya)


if __name__ == "__main__":
    game()