def fix_packages(packages: str):
    def fix(package: str):
        openPair = package.rfind("(")
        closePair = package.find(")", openPair)

        if openPair == -1:
            return package

        subPackage = package[openPair + 1 : closePair][::-1]
        return fix(package[:openPair] + subPackage + package[closePair + 1 :])

    return fix(packages)


print(
    fix_packages("a(cb)de"),  # abcde
    fix_packages("a(bc(def)g)h"),  # agdefcbh
    fix_packages("a(b(c))e"),  # acbe
    sep="\n",
)
