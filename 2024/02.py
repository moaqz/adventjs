def createFrame(names):
    maxLength = 0
    gap = 4

    for name in names:
        if len(name) > maxLength:
            maxLength = len(name)

    border = '*' * (maxLength + gap)
    body = ''

    for name in names:
        body += f"* {name.ljust(maxLength)} *\n"

    return f"{border}\n{body}{border}"

'''
***************
* midu        *
* madeval     *
* educalvolpz *
***************
'''
print(createFrame(['midu', 'madeval', 'educalvolpz']))

'''
*******
* a   *
* bb  *
* ccc *
*******
'''
print(createFrame(['a', 'bb', 'ccc']))
