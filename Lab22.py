maze = [
    "####B######################",
    "# #       #   #      #    #",
    "# # # ###### #### ####### #",
    "# # # #       #   #       #",
    "#   # # ######### # ##### #",
    "# # # #   #       #     # #",
    "### ### ### ############# #",
    "# #   #     # #           #",
    "# # #   ####### ###########",
    "# # # #       # #         C",
    "# # ##### ### # # ####### #",
    "# # #     ### # #       # #",
    "#   ##### ### # ######### #",
    "######### ### #           #",
    "# ####### ### #############",
    "A           #   ###   #   #",
    "# ############# ### # # # #",
    "# ###       # # ### # # # #",
    "# ######### # # ### # # # F",
    "#       ### # #     # # # #",
    "# ######### # ##### # # # #",
    "# #######   #       #   # #",
    "# ####### ######### #######",
    "#         #########       #",
    "#######E############D######"
]


def escape_from_maze(x, y):
    if is_normal_place(x, y):
        return

    if (x, y) in whereWas:
        return

    whereWas.append((x, y))

    if maze[y][x] != " " and maze[y][x] not in exits:
        exits.append(maze[y][x])

    escape_from_maze(x, y + 1)
    escape_from_maze(x, y - 1)
    escape_from_maze(x + 1, y)
    escape_from_maze(x - 1, y)


def is_normal_place(x, y):
    return y < 0 or x < 0 or x >= len(maze[0]) or y >= len(maze) or maze[y][x] == "#";


whereWas = []
exits = []
x, y = map(int, input().split())

if is_normal_place(x, y):
    print("Не верные координаты")
else:
    escape_from_maze(x, y)
    if (len(exits) == 0):
        print("Выхода нет")
    else:
        for exit in exits:
            print(exit, end=' ')
        print()