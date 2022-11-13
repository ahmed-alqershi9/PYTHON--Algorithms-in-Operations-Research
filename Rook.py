import numpy as np
import random as rd
import math


count = 0
RUNS = 1000000
for j in range(RUNS):
    chess_board = np.zeros((8, 8))
    for i in range(8):
        x = round(np.random.uniform(0, 63))
        chess_board[math.floor(x / 8)][np.mod(x, 8)] = 1

        condition_1 = [int(sum(i)) for i in chess_board]
        condition_2 = sum(chess_board).tolist()
        condition_2 = [int(i) for i in condition_2]
        required = [[1 for i in range(8)]]

        if (condition_1 in required) and (condition_2 in required):
            print(chess_board)
            count += 1


print(f" The probability of the pattern happening is {round((count/RUNS), 8)}")

