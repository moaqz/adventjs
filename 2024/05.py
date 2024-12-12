def organizeShoes(shoes):
    map = {"R": [], "I": []}
    organizedShoes = []

    for shoe in shoes:
        type = shoe["type"]
        size = shoe["size"]
        pairType = "R" if type == "I" else "I"

        for pair in map[pairType]:
            if pair["size"] == size:
                organizedShoes.append(size)
                map[pairType].remove(pair)
                break
        else:
            map[type].append(shoe)

    return organizedShoes


print(
    organizeShoes(
        [
            {"type": "I", "size": 38},
            {"type": "R", "size": 38},
            {"type": "R", "size": 42},
            {"type": "I", "size": 41},
            {"type": "I", "size": 42},
        ]
    ),  # [38, 42]
    organizeShoes(
        [
            {"type": "I", "size": 38},
            {"type": "R", "size": 38},
            {"type": "I", "size": 38},
            {"type": "I", "size": 38},
            {"type": "R", "size": 38},
        ]
    ),  # [38, 38]
    organizeShoes(
        [
            {"type": "I", "size": 40},
            {"type": "R", "size": 40},
            {"type": "I", "size": 40},
            {"type": "R", "size": 40},
        ]
    ),  # [40,40]
    sep="\n",
)
