def draw_race(indices, length):
    lanes = []

    for idx, position in enumerate(indices):
        lane = list("~" * length)

        if position != 0:
            lane[position] = "r"

        # Adventjs has an issue with negative indices.
        # The commented code is intended to handle negative indices
        # by converting them to their equivalent positive index.
        # if position < 0:
        #     position = length + position
        # if position != 0:
        #     lane[position] = "r"

        leadingSpaces = " " * (len(indices) - idx - 1)
        lanes.append(leadingSpaces + "".join(lane) + f" /{idx+1}")

    return "\n".join(lanes)


"""
  ~~~~~~~~~~ /1
 ~~~~~r~~~~ /2
~~~~~~~r~~ /3
"""
print(draw_race([0, 5, -3], 10))


"""
   ~~r~~~~~ /1
  ~~~~~~~r /2
 ~~~~~~~~ /3
~~~~~r~~ /4
"""
# print(draw_race([2, -1, 0, 5], 8))
