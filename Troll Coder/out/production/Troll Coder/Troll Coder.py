def printFunc(seq, letter):  # print the array
    print('{} {}'.format(letter, ' '.join(seq)))


def inputFunc(length):  # make array with Q then N zeros
    return int(length) * ['0']


def swap(num):  # can be 1 or 0, must be string not int
    if num == '0':
        return '1'
    else:
        return '0'


def main():
    N = input()  #length of the sequence
    sequence = inputFunc(N) # make array with Q then N zeros
    printFunc(sequence, 'Q')
    correctBits = int(input())
    trueBits = correctBits  # number i get from the troll
    checkingIndex = 0
    while trueBits != int(N):  # if i have the same number i have the code
        sequence[checkingIndex] = swap(sequence[checkingIndex])  #swapping 1 element
        printFunc(sequence, 'Q')  # checking after change
        correctBits = int(input())  # get troll response
        if correctBits < trueBits:  # checking if i have more correct answers or no
            sequence[checkingIndex] = swap(sequence[checkingIndex])  # if i have less i am changing back
            correctBits = trueBits
        trueBits = correctBits
        checkingIndex += 1
    printFunc(sequence, 'A')  # last print must be with A




if __name__ == '__main__':
    main()
