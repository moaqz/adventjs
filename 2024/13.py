def is_robot_back(moves: str) -> bool | list[int]:
    valid_moves = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
    invert_moves = {"R": "L", "L": "R", "U": "D", "D": "U"}
    performed_moves = set()
    position = [0, 0]
    idx = 0

    def apply_move(move: str):
        dx, dy = valid_moves[move]
        position[0] += dx
        position[1] += dy
        performed_moves.add(move)

    while idx < len(moves):
        move = moves[idx]

        if move in valid_moves:
            apply_move(move)
        elif idx + 1 < len(moves):
            modifier = move
            next_move = moves[idx + 1]

            if modifier == "*":
                apply_move(next_move)
                apply_move(next_move)

            elif modifier == "!":
                inverted_move = invert_moves[moves[idx + 1]]
                apply_move(inverted_move)

            elif modifier == "?":
                if next_move not in performed_moves:
                    apply_move(next_move)

            # skip the modifier.
            idx += 1

        idx += 1

    if position == [0,0]:
        return True

    return position


print(
    is_robot_back("R"),  # [1, 0]
    is_robot_back("RL"),  # true
    is_robot_back("RLUD"),  # true
    is_robot_back("*RU"),  # [2, 1]
    is_robot_back("R*U"),  # [1, 2]
    is_robot_back("LLL!R"),  # [-4, 0]
    is_robot_back("R?R"),  # [1, 0]
    is_robot_back("U?D"),  # true
    is_robot_back("R!L"),  # [2,0]
    is_robot_back("U!D"),  # [0,2]
    is_robot_back("R?L"),  # true
    is_robot_back("U?U"),  # [0,1]
    is_robot_back("*U?U"),  # [0,2]
    is_robot_back("U?D?U"),  # true
    sep="\n",
)
