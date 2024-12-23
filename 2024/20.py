def fix_gift_list(received: list[str], expected: list[str]) -> dict[str, int]:
    missing_items = {}
    extra_items = {}
    all_items = set(received) | set(expected)

    for item in all_items:
        expected_items = expected.count(item)
        received_items = received.count(item)

        if received_items < expected_items:
            missing_items[item] = abs(expected_items - received_items)
        elif received_items > expected_items:
            extra_items[item] = abs(expected_items - received_items)

    return {"missing": missing_items, "extra": extra_items}


"""
{
  "missing": { ball: 1 }
  "extra": { car: 1 }
}
"""
print(
    fix_gift_list(["puzzle", "car", "doll", "car"], ["car", "puzzle", "doll", "ball"])
)

"""
{
  "missing": { ball: 1, kite: 1 },
  "extra": { train: 1 }
}
"""
print(
    fix_gift_list(
        ["book", "train", "kite", "train"], ["train", "book", "kite", "ball", "kite"]
    )
)


"""
{
  "missing": { },
  "extra": { }
}
"""
print(fix_gift_list(["bear", "bear", "car"], ["car", "bear", "bear"]))
