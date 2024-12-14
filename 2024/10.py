from typing import List


def compile(instructions: List[str]) -> None | int:
    def is_number(n: str):
        return n.lstrip("-").isdigit()

    registers = {}
    idx = 0

    while idx < len(instructions):
        parts = instructions[idx].split()
        action = parts[0]

        if action == "MOV":
            x, y = parts[1], parts[2]
            registers[y] = int(x) if is_number(x) else registers.get(x, 0)

        elif action == "INC":
            key = parts[1]
            registers[key] = registers.get(key, 0) + 1

        elif action == "DEC":
            key = parts[1]
            registers[key] = registers.get(key, 0) - 1

        elif action == "JMP":
            key, target = parts[1], int(parts[2])
            if registers.get(key, 0) == 0:
                idx = target
                continue

        idx += 1

    return registers.get("A")


print(
    compile(["MOV -1 C", "INC C", "JMP C 1", "MOV C A", "INC A"]),  # 2
    compile(["INC A", "INC A", "DEC A", "MOV A B"]),  # 1
    compile(["MOV 5 B", "DEC B", "MOV B A", "INC A"]),  # 5
    sep="\n",
)
