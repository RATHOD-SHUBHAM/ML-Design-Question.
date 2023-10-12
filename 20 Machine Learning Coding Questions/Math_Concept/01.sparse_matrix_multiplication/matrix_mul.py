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

