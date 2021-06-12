# normal caul of catalan numbers


def catalan_cal(n, array):
    index = len(array)
    if index == n + 1:
        return array[n]

    sum = 0
    for i in range(0, index):
        sum += array[i] * array[index - i - 1]

    array.append(sum)
    return catalan_cal(n, [1])

def catalan_num(n):
    if n == 0:
        return 1
    return catalan_cal(n, [1])

def catalan(num):
    array = [1]
    for n in range(5, 1000):
        index = len(array)
        if array[index - 1] == num:
            return index - 1

        sum = 0
        for i in range(0, index):
            sum += (array[i] * array[index - i - 1])

        array.append(sum)


try:
    while True:
        n = int(input())
        if n == 1:
            print(3)
        elif n == 2:
            print(4)
        elif n == 5:
            print(5)
        else:
            print(catalan(n) + 2)


except EOFError:
    pass