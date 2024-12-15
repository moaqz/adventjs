def min_moves_to_stables(reindeer: list, stables: list) -> int:
    reindeer.sort()
    stables.sort()

    total_moves = 0
    for i in range(len(reindeer)):
        total_moves += abs(reindeer[i] - stables[i])

    return total_moves


print(
    min_moves_to_stables([2, 6, 9], [3, 8, 5]),  # 3
    min_moves_to_stables([1, 1, 3], [1, 8, 4]),  # 8
    sep="\n",
)
