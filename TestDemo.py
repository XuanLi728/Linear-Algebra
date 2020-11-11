import numpy as np
import random
from itertools import permutations

Identity_matrix = np.eye(3)

# Test_Matrix =np.random.randint(1,5,(3,3))
Test_Matrix = [ [1, 0, 0], [2, 0, 0], [3, 0, 0]]

print("Origin Matrix: \n", Test_Matrix)

per = permutations(range(3), 3) # n! 

Permutation_matrix = [ Identity_matrix[i,:] for i in per ]  # 置换矩阵

for Matrix in Permutation_matrix:

    print("Matrix : \n",Matrix)

    Row_Change_Matrix = np.dot(Matrix, Test_Matrix) # 线代定义的矩阵相乘，即内积

    # Row_Change_Matrix = Matrix * Test_Matrix  # 对应元素直接相乘， 并非线代定义的矩阵相乘
    # print("Before: \n", Identity_matrix , " X " , Matrix)
    
    print("After:  \n", Row_Change_Matrix)

    print("------------------")

