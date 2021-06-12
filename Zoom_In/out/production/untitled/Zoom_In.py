n = int(input())
m = int(input())
k = int(input())

letters = {}
for i in range(0,k):
    key = input()
    letter = []
    for j in range(0,n):
        letter.append(input())
    print(letter)
    letters[key] = letter
    print(letters)