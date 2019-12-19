# 1 2 3 4 5
from math import sqrt

for i in range(5):
    print(i + 1, end=' ')
print('\n')

# 1 1 2 2 3 3 4 4 5 5
for i in range(5):
    print(i + 1, end=' ')
    print(i + 1, end=' ')

print('\n')
# 1/ 2  2 / 3 3 3 / 4 4 4 4
for i in range(4):
    for j in range(i + 1):
        print(i + 1, end=' ')
print('\n')

# 1 1 /2 2 2 2 /3 3 3 3 3 3/ 4 4 4 4 4 4 4 4
for i in range(4):
    for j in range(i + 1):
        print(i + 1, i + 1, end=' ')
print('\n')

# 1 2 / 3 3 4 4 / 5 5 5 6 6 6 / 7 7 7 7 8 8 8 8

# n 은 근의 공식에 의해
distance = int(input('이동 거리?: '))
n = int((sqrt(1 + 4 * distance) - 1) / 2)+1
# n = int(distance/2)
print('n: ',n)
num_of_moves = []
for i in range(n):
    for j in range(i + 1):
        x = 2 * (i + 1) - 1
        print(x, end=' ')
        num_of_moves.append(x)
    for j in range(i + 1):
        y = 2 * (i + 1)
        print(y, end=' ')
        num_of_moves.append(y)
print('\n')
print("distance: ", num_of_moves[distance])
