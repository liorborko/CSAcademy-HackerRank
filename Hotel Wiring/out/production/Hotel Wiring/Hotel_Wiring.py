def parser():
    while 1:
        try:
            data = list(input().split(' '))
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
if T in range(1, 20):
    for i in range(1, T):
        totalsum = 0
        switches = get_number()
        rooms = get_number()
        floors = get_number()
        sum = []
        for i in range(0, floors):
            m = int(input())
            sum[i].append(m)

        sum.sort()
        for k in range(0, floors):
            if k < switches:
                totalsum = totalsum + (rooms - sum[k])
            else:
                totalsum = totalsum + sum[i]
        print(totalsum)

