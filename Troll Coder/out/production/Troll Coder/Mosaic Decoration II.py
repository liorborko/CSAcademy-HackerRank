import math

inputAArray = list(map(int, input().rstrip().split()))

# Bathroom Width
W = inputAArray[0]

# Bathroom Height
H = inputAArray[1]

# Tiles Width
A = inputAArray[2]

# Tiles Height
B = inputAArray[3]

# Purchase cost
M = inputAArray[4]

# Worker cost
C = inputAArray[5]

# Tiles
row = int(W/A)
col = int(B/H)

num = row * col

# difference
rowDiff = W - (A*row)
# print(rowDiff)
# print(math.ceil(W/A))
colDiff = H - (B*col)

Diff = 0

if rowDiff != 0:
    Diff = Diff + H
if colDiff != 0:
    col = col + W

totalCost = int(num/10) * M + Diff * C
print(totalCost)







