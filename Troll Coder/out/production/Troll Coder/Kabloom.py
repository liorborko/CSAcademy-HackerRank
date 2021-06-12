def check(a, b):
    if a == b == 'R':
        return 50
    elif a == 'R':
        if b == 'A': return 20
        if b == 'Q': return 15
        if b == 'K': return 15
        if b == 'J': return 15
        if b == 'T': return 10
        return b - '0'
    if b == 'R':
        if a == 'A': return 20
        if a == 'Q': return 15
        if a == 'K': return 15
        if a == 'J': return 15
        if a == 'T': return 10
        return a - '0'

    elif a == 'A':
        return 20
    elif a == 'T':
        return 10
    elif a == 'J':
        return 15
    elif a == 'Q':
        return 15
    else:
        if a == 'K': return 15


def max(a, b):
    if a >= b:
        return a
    else:
        return b


try:
    firstRow = list(input().split())
    secRow = list(input().split())
    sumArray = [[], []]
    while input() is not '0':
        n = input()
        if n != 0:
            for i in firstRow:
                for j in secRow:
                    sumArray[i][j] = max(sumArray[i - 1][j], sumArray[i][j - 1])
                    if firstRow[i][0] == secRow[j][0] or firstRow[i][0] == 'R' or secRow[j][0] == 'R':
                        sumArray[i][j] = max(sumArray[i][j],
                                             sumArray[i - 1][j - 1] + check(firstRow[i][0], secRow[j][0]))
except EOFError:
    exit()

print(sumArray)
