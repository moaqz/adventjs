def calculate_price(ornaments: str) -> int:
    price = 0
    idx = 0
    ornament_values = {"*": 1, "o": 5, "^": 10, "#": 50, "@": 100}

    while idx < len(ornaments):
        current_ornament = ornaments[idx]

        if current_ornament not in ornament_values:
            return None

        current_ornament_price = ornament_values[current_ornament]

        if idx + 1 < len(ornaments):
            next_ornament = ornaments[idx + 1]
            if next_ornament not in ornament_values:
                return None

            next_ornament_price = ornament_values[next_ornament]
            if current_ornament_price < next_ornament_price:
                price -= current_ornament_price
            else:
                price += current_ornament_price
        else:
            price += current_ornament_price

        idx += 1

    return price


print(
    calculate_price("***"),  # 3   (1 + 1 + 1)
    calculate_price("*o"),  # 4   (5 - 1)
    calculate_price("o*"),  # 6   (5 + 1)
    calculate_price("*o*"),  # 5  (-1 + 5 + 1)
    calculate_price("**o*"),  # 6  (1 - 1 + 5 + 1)
    calculate_price("o***"),  # 8   (5 + 3)
    calculate_price("*o@"),  # 94  (-5 - 1 + 100)
    calculate_price("*#"),  # 49  (-1 + 50)
    calculate_price("@@@"),  # 300 (100 + 100 + 100)
    calculate_price("#@"),  # 50  (-50 + 100)
    calculate_price("#@Z"),  # undefined
    sep="\n",
)
