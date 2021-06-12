# number of test
T = int(input())

for test in range(T):
    # number of piles
    G = int(input())
    pile = []
    total_piles = 0
    turns = 0
    # input as string so we need string
    string = ''

    # input number as string
    for x in range(G):
        total_piles += int(input())
        string += " " + input()
    # convert the string into numbers
    for num in string.split():
        pile.append(int(num))

    # check if number of turns is even or odd
    for i in pile:
        turns += int(i) // 2  # opertor // gives me floor division

    if turns % 2:
        print('Alice')
    else:
        print('Bob')
