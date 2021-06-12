import math

W,H,A,B,M,C = list(map(int, input().rstrip().split()))

# W = Bathroom Width
# H = Bathroom Height
# A = Tiles Width
# B = Tiles Height
# M = Purchase cost
# C = Worker cost


# Tiles
row = math.ceil(W / A)

col = math.ceil(H / B)


num = row * col

# difference
rowDiff = (A * row) - W
colDiff = (B * col) - H

Diff = 0

if rowDiff != 0:
    Diff = Diff + H
if colDiff != 0:
    Diff = Diff + W

totalCost = math.ceil(num / 10) * M + Diff * C
print(totalCost)
