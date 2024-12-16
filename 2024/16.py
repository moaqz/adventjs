def remove_snow(s: str) -> str:
    if len(s) <= 1:
        return s

    idx = 0
    while idx < len(s) - 1:
        if s[idx + 1] == s[idx]:
            return remove_snow(s[:idx] + s[idx + 2 :])

        idx += 1

    return s


print(
    remove_snow("zxxzoz"),  # -> "oz"
    remove_snow("abcdd"),  # -> "abc"
    remove_snow("zzz"),  # -> "z"
    remove_snow("a"),  # -> "a"
    sep="\n",
)
