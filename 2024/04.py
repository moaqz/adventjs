def create_xmas_tree(height: int, ornament: str):
    tree: list[str] = []
    max_width = height * 2 - 1

    for i in range(1, height + 1):
        layer = ornament * (2 * i - 1)
        tree.append(layer.center(max_width, "_"))

    trunk = ["#".center(max_width, "_")] * 2
    tree.extend(trunk)

    return "\n".join(tree)


"""
____*____
___***___
__*****__
_*******_
*********
____#____
____#____
"""
print(create_xmas_tree(5, "*"))

"""
_____@_____
____@@@____
___@@@@@___
__@@@@@@@__
_@@@@@@@@@_
@@@@@@@@@@@
_____#_____
_____#_____
"""
print(create_xmas_tree(6, "@"))
