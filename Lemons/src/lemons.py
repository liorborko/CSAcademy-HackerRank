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


def quickSearch(start, end, flag):
    if start > end:
        return 0
    else:
        mid = (start + end) // 2
        time = (mid - flag) * M + S
        # print(time)
        start = mid
        flag = mid
        return time + quickSearch(start+1, end, flag)

try:
    inputData = list(map(int, input().split()))
    N = inputData[0]  # number of water pumps
    M = inputData[1]  # time to reach from one water pump to next water pump
    S = inputData[2]  # time takes to check water pump

    start = 2
    end = N

    time = quickSearch(start, end, 1)
    print(time)
except EOFError:
    print(EOFError)


