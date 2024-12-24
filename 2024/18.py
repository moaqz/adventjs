def find_in_agenda(agenda: str, phone: str) -> dict | None:
    lines = agenda.strip().splitlines()
    matches = []

    for line in lines:
        if phone in line:
            matches.append(line)
            if len(matches) > 1:
                return None

    if len(matches) == 1:
        matched_line = matches[0]

        name = matches[0][matched_line.index("<") + 1 : matched_line.find(">")]
        address = ""

        for word in matched_line.split(" "):
            if word.startswith("+") or word.startswith("<") or word.endswith(">"):
                continue
            address += f" {word}"

        return {"name": name, "address": address.strip(" ")}

    return None


agenda = """
+34-600-123-456 Calle Gran Via 12 <Juan Perez>
Plaza Mayor 45 Madrid 28013 <Maria Gomez> +34-600-987-654
<Carlos Ruiz> +1-800-555-0199 Fifth Ave New York
"""

print(
    find_in_agenda(
        agenda, "34-600-123-456"
    ),  # { name: "Juan Perez", address: "Calle Gran Via 12" }
    find_in_agenda(
        agenda, "600-987"
    ),  # { name: "Maria Gomez", address: "Plaza Mayor 45 Madrid 28013" }
    find_in_agenda(agenda, "111"),  # None
    find_in_agenda(agenda, "1"),  # None
    sep="\n",
)
