######################################################################
# Author: Tradd Schmidt
# username: schmidtt

# Assignment: L02
# Purpose: To get more practice with stacks and nested lists
######################################################################

from Explorer import Explorer
from Stack import Stack
import copy


def print_map(win_map, path, start_row, start_col):
    """
    Prints a map of paths that lead to treasure
    :param start_row: The starting row of the map
    :param start_col: The starting column of the map
    :param path: the stack of directions that have been made
    :param win_map: The map that has the winning paths on it
    :return: none
    """
    if path.size() == 0:
        return
    else:
        path = copy.deepcopy(path)
        path.items.reverse()
        winner = Explorer(start_row, start_col)
        print("The following is the total paths to treasure. Underscore's denote the path to a treasure:")
        for i in range(path.size() - 1):
            forward = path.pop()
            if forward == "north":
                winner.move_n()
            elif forward == "south":
                winner.move_s()
            elif forward == "east":
                winner.move_e()
            elif forward == "west":
                winner.move_w()
            win_map[winner.row][winner.col] = "_"
    for i in win_map:
        print(i)


def find_start(cave_map):
    """
    Iterates through the map to find the colum and row where the "explorer" will start
    :param cave_map: list with nested lists that is the map of the cave
    :return: the row and column of the starting location of "M"
    """
    row = 0
    for i in cave_map:
        col = 0
        for j in i:
            if j == "M":
                return row, col
            col += 1
        row += 1


def parse_file(words_file_name):
    """
    Parses a text file line by line and adds it to a list to be returned
    :param words_file_name: The file that will be parsed
    :return: The lines of the text file minus the first line
    """
    words_list = []
    try:
        open_file = open(words_file_name, 'r')
        contents = open_file.readline()
        contents = contents[:-1]
        while contents:
            words_list.append(contents.split())
            contents = open_file.readline()
            contents = contents[:-1]
        open_file.close()
    except IOError:
        print("File does not exist! Try again.")
    words_list = words_list[1:]
    return words_list


def update_map(explorer, cave_map, direction):
    """
    Updates the map to reflect the movement of the explorer through the map
    :param explorer: The "M" in the map
    :param cave_map: the map that is being updated
    :param direction: what direction the explorer is moving in
    :return: none
    """
    if direction == "north":
        cave_map[explorer.row - 1][explorer.col] = "M"
        cave_map[explorer.row][explorer.col] = "."
    elif direction == "south":
        cave_map[explorer.row + 1][explorer.col] = "M"
        cave_map[explorer.row][explorer.col] = "."
    elif direction == "east":
        cave_map[explorer.row][explorer.col + 1] = "M"
        cave_map[explorer.row][explorer.col] = "."
    elif direction == "west":
        cave_map[explorer.row][explorer.col - 1] = "M"
        cave_map[explorer.row][explorer.col] = "."


def treasure_path(path):
    """
    Displays the verbal directions to reach a treasure point from the starting position
    :param path: a stack of the directions taken to reach treasure
    :return: none
    """
    win = copy.deepcopy(path)
    win.items.reverse()
    print("The following is a path to get to a treasure:")
    for i in range(win.size()):
        print(win.pop())


def check_surrounding(explorer, cave_map):
    """
    Checks the surrounding 4 points to check if they have been visited or not
    :param explorer: The "M" in the map
    :param cave_map: the map that will be used to check
    :return:
    """
    n, n_pos = cave_map[explorer.row - 1][explorer.col], [explorer.row - 1, explorer.col]
    s, s_pos = cave_map[explorer.row + 1][explorer.col], [explorer.row + 1, explorer.col]
    e, e_pos = cave_map[explorer.row][explorer.col + 1], [explorer.row, explorer.col + 1]
    w, w_pos = cave_map[explorer.row][explorer.col - 1], [explorer.row, explorer.col - 1]

    if n_pos not in explorer.memory:
        if n != "W" and n != "_":
            return False
    elif s_pos not in explorer.memory:
        if s != "W" and n != "_":
            return False
    elif e_pos not in explorer.memory:
        if e != "W" and n != "_":
            return False
    elif w_pos not in explorer.memory:
        if w != "W" and n != "_":
            return False
    else:
        return True


def advance(explorer, cave_map, path, win_map, start_row, start_col):
    """

    :param explorer: The "M" in the map
    :param cave_map: the map that is being traversed
    :param path: the stack of directions that have been made
    :param win_map: The map that has the winning paths on it
    :param start_row: The starting row of the map
    :param start_col: The starting column of the map
    :return: a boolean
    """
    n, n_pos = cave_map[explorer.row - 1][explorer.col], [explorer.row - 1, explorer.col]
    s, s_pos = cave_map[explorer.row + 1][explorer.col], [explorer.row + 1, explorer.col]
    e, e_pos = cave_map[explorer.row][explorer.col + 1], [explorer.row, explorer.col + 1]
    w, w_pos = cave_map[explorer.row][explorer.col - 1], [explorer.row, explorer.col - 1]

    # Checks to see if there is any treasure in the surrounding area
    if n == "T":
        if n_pos not in explorer.memory:
            explorer.move_n()
            explorer.remember()
            path.push("north")
            print_map(win_map, path, start_row, start_col)
            treasure_path(path)
            backtrack(explorer, cave_map, path)
            return True
    elif s == "T":
        if s_pos not in explorer.memory:
            explorer.move_s()
            explorer.remember()
            path.push("south")
            print_map(win_map, path, start_row, start_col)
            treasure_path(path)
            backtrack(explorer, cave_map, path)
            return True
    elif e == "T":
        if e_pos not in explorer.memory:
            explorer.move_e()
            explorer.remember()
            path.push("east")
            print_map(win_map, path, start_row, start_col)
            treasure_path(path)
            backtrack(explorer, cave_map, path)
            return True
    elif w == "T":
        if w_pos not in explorer.memory:
            explorer.move_w()
            explorer.remember()
            path.push("west")
            print_map(win_map, path, start_row, start_col)
            treasure_path(path)
            backtrack(explorer, cave_map, path)
            return True

    # Checks to see if there is an available space to move to
    if n == ".":
        if n_pos not in explorer.memory:
            update_map(explorer, cave_map, "north")
            explorer.move_n()
            explorer.remember()
            path.push("north")
            return True
    if s == ".":
        if s_pos not in explorer.memory:
            update_map(explorer, cave_map, "south")
            explorer.move_s()
            explorer.remember()
            path.push("south")
            return True
    if e == ".":
        if e_pos not in explorer.memory:
            update_map(explorer, cave_map, "east")
            explorer.move_e()
            explorer.remember()
            path.push("east")
            return True
    if w == ".":
        if w_pos not in explorer.memory:
            update_map(explorer, cave_map, "west")
            explorer.move_w()
            explorer.remember()
            path.push("west")
            return True
    if path.size() != 0:
        backtrack(explorer, cave_map, path)
        return True
    else:
        return False


def backtrack(explorer, cave_map, path):
    """

    :param explorer: The "M" in the map
    :param cave_map: the map that is being backtracked through
    :param path: the stack of directions that have been made
    :return: none
    """
    check = True
    while check:
        if path.size() == 0:
            break
        move = path.pop()
        if move == "north":
            update_map(explorer, cave_map, "south")
            explorer.move_s()
        elif move == "south":
            update_map(explorer, cave_map, "north")
            explorer.move_n()
        elif move == "east":
            update_map(explorer, cave_map, "west")
            explorer.move_w()
        elif move == "west":
            update_map(explorer, cave_map, "east")
            explorer.move_e()
        check = check_surrounding(explorer, cave_map)


def main():
    cave_map = parse_file("cave_2.txt")
    win_map = copy.deepcopy(cave_map)
    start_row, start_col = find_start(cave_map)
    test = Explorer(start_row, start_col)
    path = Stack()
    not_finished = True
    while not_finished:
        not_finished = advance(test, cave_map, path, win_map, start_row, start_col)
    print("There was no more treasure.")


if __name__ == "__main__":
    main()
