import random
import math

evenNum = [[0]*6 for i in range(6)]

print()


for i in range(1, 6):
    for j in range(1, 6):
        evenNum[i][j] = i*j


for i in range(1, 6):
    for j in range(1, 6):
        print(f"{j} x {i} =" , evenNum[i][j], end=" || ")

    print()