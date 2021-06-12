def check(num):
    if len(str(num)) == num:  # checking if the length of the string equal to the number in the string
        return 1
    else:
        if num == '1':  # 1 will be always the last number because |0| and |1| = 1
            return 1
        return 1 + check(len(str(num)))


raw = input()
while raw != 'END':  # input function and check first input
    # number = int(raw)
    print(check(raw))
    raw = input()


