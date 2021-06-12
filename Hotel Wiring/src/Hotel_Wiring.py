def parser():
    while 1:
        try:
            data = list(input().split())
            for number in data:
                if len(number) > 0:
                    yield number
        except EOFError:
            return


input_parser = parser()


def get_word():
    global input_parser
    return next(input_parser)


def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)


T = get_number()

for i in range(T):
    array = list(map(int, input().split()))
    sum = []  # rooms array
    totalsum = 0
    if array[0] == 0 or array[1] == 0:  # checking if there is 0 floors or rooms on the floor
        print(totalsum)
    else:
        for i in range(array[0]):
            m = int(input())  # sum rooms on each floor
            sum.append(m)

        sum.sort()
        for k in range(array[0]):  # if k > array[0] then we check every floor
            if k < array[2]:  # checking if k is not bigger then number of switch need to turn on
                if array[1] < sum[k]:  # number of room on the floor smaller then rooms not wired
                    totalsum = totalsum - array[1]
                    if totalsum < 0:
                        totalsum = 0
                # elif k <
                else:
                    # number of rooms per floor - rooms wired (they wont  be if we switch)
                    totalsum = totalsum + (array[1] - sum[k])
            else:
                totalsum = totalsum + sum[k] # counter the total sum and number of rooms can be wired
        print(totalsum)

