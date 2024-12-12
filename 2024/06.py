def in_box(box: list[str]):
    giftX, giftY = -1, -1
    boxWidth, boxHeight = len(box[0]) - 1, len(box) - 1

    for idx, line in enumerate(box):
        if "*" in line:
            giftY = idx
            giftX = line.index("*")
            break

    if giftX == -1 or giftY == -1:
        return False

    if (giftX > 0 and giftX < boxWidth) and (giftY > 0 and giftY < boxHeight):
        return True

    return False


print(
    in_box(["###", "#*#", "###"]),  # true
    in_box(["####", "#* #", "#  #", "####"]),  # true
    in_box(["#####", "#   #", "#  #*", "#####"]),  # false
    in_box(["#####", "#   #", "#   #", "#   #", "#####"]),  # false
    sep="\n",
)
