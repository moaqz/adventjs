def tree_height(tree: dict):
    if tree is None:
        return 0

    left_height = tree_height(tree.get("left"))
    right_height = tree_height(tree.get("right"))

    return 1 + max(left_height, right_height)


# --> 3
print(
    tree_height(
        {
            "value": "🎁",
            "left": {
                "value": "🎄",
                "left": {"value": "⭐", "left": None, "right": None},
                "right": {"value": "🎅", "left": None, "right": None},
            },
            "right": {
                "value": "❄️",
                "left": None,
                "right": {"value": "🦌", "left": None, "right": None},
            },
        }
    )
)
