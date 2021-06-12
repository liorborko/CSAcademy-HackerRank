def printFunc(seq, letter):
    print('{} {}'.format(letter, ' '.join(seq)))


def inputFunc(length):
    return int(length) * ['0']


def swap(num):
    if num == '0':
        return '1'
    else:
        return '0'


def main():
    N = input()
    sequence = inputFunc(N)
    printFunc(sequence, 'Q')
    correctBits = int(input())
    trueBits = correctBits
    checkingIndex = 0
    while trueBits != int(N):
        sequence[checkingIndex] = swap(sequence[checkingIndex])
        printFunc(sequence, 'Q')
        correctBits = int(input())
        if correctBits < trueBits:
            sequence[checkingIndex] = swap(sequence[checkingIndex])
            correctBits = trueBits
        trueBits = correctBits
        checkingIndex += 1
    printFunc(sequence, 'A')




if __name__ == '__main__':
    main()
