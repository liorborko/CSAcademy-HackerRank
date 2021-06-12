
test = input()
test = int(test)
colors = []
counter = int(0)


sequence = int(0)
while sequence < test:

    numOfColors = input()  # total colors
    numOfColors = int(numOfColors)
    colors = input().split(' ')
    for color in colors:  # convert every element from string to int
        color = int(color)
    hasBrush = colors[0]
    counter += 1
    nextBrush: int = -1  # -1 because we didnt check next brush yet (can also be 0)

    for num in range(0, numOfColors):
        if colors[num] == hasBrush or colors[num] == nextBrush:  # checking if i have this color on one brush
            continue
        else:
            for k in range(0, 20):
                try:
                    if hasBrush == colors[num + k]:  # i am using num + k because it's for in for
                        break

                    elif nextBrush == colors[num + k]:
                        # swap
                        temp = nextBrush
                        nextBrush = hasBrush
                        hasBrush = temp
                        break

                except Exception:
                    break

            nextBrush = colors[num]
            counter += 1

    sequence += 1
    print(counter)
    counter = 0




