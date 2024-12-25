def find_missing_numbers(nums: list[int]):
    diff = set(range(1, max(nums) + 1)).difference(nums)
    return list(diff)


print(
    find_missing_numbers([1, 2, 4, 6]),  # [3, 5]
    find_missing_numbers([4, 8, 7, 2]),  # [1, 3, 5, 6]
    find_missing_numbers([3, 2, 1, 1]),  # []
    find_missing_numbers([5, 5, 5, 3, 3, 2, 1]),  # [4]
    sep="\n",
)
