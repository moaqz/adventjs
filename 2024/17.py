def detect_bombs(grid: list[list[bool]]) -> list[list[int]]:
    detected_bombs = [row[:] for row in grid]

    # (y, x)
    directions = [
        (-1, 0),  # up
        (1, 0),  # down
        (0, 1),  # right
        (0, -1),  # left
        (-1, 1),  # top-right
        (-1, -1),  # top-left
        (1, 1),  # bottom-right
        (1, -1),  # bottom-left
    ]

    row_size = len(grid)
    column_size = len(grid[0])

    # for rows -> (y)
    # for columns -> (x)
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            adjacent_bombs = 0

            for dy, dx in directions:
                new_y, new_x = y + dy, x + dx
                valid_column = new_x >= 0 and new_x < column_size
                valid_row = new_y >= 0 and new_y < row_size

                if valid_column and valid_row:
                    if grid[new_y][new_x]: # True
                        adjacent_bombs += 1

            detected_bombs[y][x] = adjacent_bombs

    return detected_bombs


"""
[
  [1, 2, 1],
  [2, 1, 1],
  [1, 1, 1]
]
"""
print(detect_bombs([[True, False, False], [False, True, False], [False, False, False]]))

"""
[
  [0, 1],
  [1, 1]
]
"""
print(detect_bombs([[True, False], [False, False]]))

"""
[
  [1, 1],
  [4, 4],
  [1, 1]
]
"""
print(detect_bombs([[True, True], [False, False], [True, True]]))
