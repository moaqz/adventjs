def prepare_gifts(gifts):
    uniqueGifts = set(gifts)
    return sorted(uniqueGifts)

print(
    prepare_gifts([3, 1, 2, 3, 4, 2, 5]), # [1, 2, 3, 4, 5]
    prepare_gifts([6, 5, 5, 5, 5]), #  [5, 6]
    prepare_gifts([]), # []
    sep="\n"
)
