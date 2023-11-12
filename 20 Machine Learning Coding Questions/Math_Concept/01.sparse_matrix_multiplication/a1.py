# ----------------- Matrix Multiplication ------------------------

from typing import List

class Solution:
    def multiply(self, matrix_a, matrix_b) -> List:
        # dimension of matrix
        m1, n1 = len(matrix_a) , len(matrix_a[0])
        m2, n2 = len(matrix_b) , len(matrix_b[0])

        # n1 and m2 should be same
        if n1 != m2:
            return False
        
        # matrix_c dimension = m1 X n2
        matrix_c = [[0 for _ in range(n2)]for _ in range(m1)]

        for i in range(m1):
            for j in range(n2):
                for x in range(n1): # n1 or m2
                    matrix_c[i][j] += matrix_a[i][x] * matrix_b[x][j]
        
        return matrix_c




if __name__ == '__main__':
    matrix_a = [[1,2,3], [4,5,6]]
    matrix_b = [[7,8], [9,10], [11,12]]

    obj = Solution()

    print(obj.multiply(matrix_a, matrix_b))


# ----------------- Sparse Matrix Multiplication ------------------------

'''
    A matrix is a two-dimensional data object made of m rows and n columns, therefore having total m x n values. 
    If most of the elements of the matrix have 0 value, then it is called a sparse matrix
'''

def sparse_matrix_multiplication(matrix_a, matrix_b):
    # Dimension
    a , b = len(matrix_a), len(matrix_a[0])
    m , n = len(matrix_b) , len(matrix_b[0])
    # Multiplication is not possible
    if b != m:
        return [[]]

    sparse_a = get_nonzero_cells(matrix_a)
    # print(sparse_a)
    sparse_b = get_nonzero_cells(matrix_b)
    # print(sparse_b)

    matrix_c = [[0 for _ in range(n)] for _ in range(a)]
    # print(matrix_c)

    for a, m in sparse_a.keys():
        for n in range(len(matrix_b[0])):

            if (m,n) in sparse_b.keys():

                # matrix_c[a][n] += sparse_a[(a,m)] * sparse_b[(m,n)]
                # or
                matrix_c[a][n] += matrix_a[a][m] * matrix_b[m][n]

    return matrix_c
        

    

def get_nonzero_cells(matrix):
    non_zero_cell = {}
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):

            if matrix[i][j] != 0:
                non_zero_cell[(i,j)] = matrix[i][j]

    return non_zero_cell