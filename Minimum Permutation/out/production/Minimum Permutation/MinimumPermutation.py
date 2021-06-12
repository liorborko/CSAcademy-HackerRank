
# input and convert every input to int
N = input().split()
N = int(N)

M = input().split()
M = int(M)

# input array and convert string in list(array) to int
arrayA = input().split()
arrayA = list(map(int,arrayA))

# input set and convert string in list to int
setB = input().split()
setB = list(map(int, setB))

# make life easy
setB.sort()

i=0
while 0 < len(setB):
    if setB[0] < arrayA[i]:
        arrayA.insert(i, setB[0])
        setB.pop(0)
        print(arrayA)
        print(setB)

        i=0

    i +=1

for element in arrayA:
    print(element)
