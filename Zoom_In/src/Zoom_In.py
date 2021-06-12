n = int(input())
m = int(input())
k = int(input())

# word = []
paintLetter = {}
for i in range(0, k):
    letter = input()
    # word.append(letter)
    letterArray = []
    for j in range(0,m):
        letterArray.append(input())
    # print(letterArray)
    paintLetter[letter] = letterArray
    # print(word)

stringsNum = int(input())
strings = []

for i in range(stringsNum):
    # strings.append(list(map(list,input().rstrip().split())))
    strings.append(input())

# if stringsNum != 1:
#     breakpoint('more then 1 string')

# for i in range(len(strings)):
#     if strings[0][0][i] == word[i]:
#         continue
#     else:
#         print('not the same word')

for string in strings:  #for each string
    for i in range(0, m):
        newline = ''
        for j in string:
            newline += paintLetter[j][i]

        print(newline)











