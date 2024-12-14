from typing import List, Literal

def move_train(board: List[str], mov: Literal["U", "D", "R", "L"]) -> Literal["none", "crash", "eat"]:
  directions = {
    "U": (-1, 0),
    "D": (1, 0),
    "R": (0, 1),
    "L": (0, -1),
  }

  # matrix is n * m
  n, m = len(board), len(board[0])

  for i, row in enumerate(board):
    for j, col in enumerate(row):
      if col == "@":
        dy, dx = directions[mov]
        new_y, new_x = i + dy, j + dx

        if new_y < 0 or new_y > n or new_x < 0 or new_x > m:
          return "crash"
        
        next_col = board[new_y][new_x]
        if next_col == "*":
          return "eat"
        elif next_col == "o":
          return "crash"
        
  return "none"


board = [
  "·····",
  "*····",
  "@····",
  "o····",
  "o····"
]

print(
  move_train(board, "U"), # eat
  move_train(board, "D"), # crash
  move_train(board, "L"), # crash
  move_train(board, "R"), # none
  sep="\n" 
)
