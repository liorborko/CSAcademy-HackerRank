# input and convert every input to int
N, M = input().split()
N = int(N)
M = int(M)

# input array and convert string in list(array) to int
arrayA = input().split(' ')
arrayA = list(map(int, arrayA))

# input set and convert string in list to int
setB = input().split(' ')
setB = list(map(int, setB))

# make life easy
setB.sort()

newList = []

a = 0
b = 0
for i in range(N+M):  # all elements are between 1 and N+M
    if b == M:  # if M == 0  we the set is empty
        for k in range(i, M+N):
            newList.insert(k, arrayA[a])
            a += 1
        break

    if a == N:  # if N ==0 the array is empty
        for k in range(i, M+N):
            newList.insert(k, setB[b])
            b += 1
        break

    if setB[b] < arrayA[a]:  # if element in set smaller then element in array
        newList.insert(i, setB[b])  # insert element from set to new list
        b += 1
    else:
        newList.insert(i, arrayA[a])  # insert element from array to new list
        a += 1

# print new list
for element in newList:
    print(element)






# while 0 < len(setB):  # if setB is empty there is nothing to insert
#     if setB[0] == arrayA[i]:
#         setB.pop(0)
#
#     elif setB[0] < arrayA[i]:  # setB is sort, setb[0] is the first to insert
#         arrayA.insert(i, setB[0])  # insert first element from setB in place i
#         setB.pop(0)
#
#     i += 1
#
# for element in arrayA:
#     print(element)
