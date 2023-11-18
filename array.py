import random

matrix = [[random.randint(1, 100) for _ in range(5)] for _ in range(5)]

# Matrixni ekranga chiqarish
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()
