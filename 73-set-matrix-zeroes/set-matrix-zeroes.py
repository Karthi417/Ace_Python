class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        m=len(matrix[0])
        def markrow(matrix,n,m,i):
            for j in range(m):
                if matrix[i][j]!=0:
                    matrix[i][j]=None
        def markcolumn(matrix,n,m,j):
            for i in range(n):
                if matrix[i][j]!=0:
                    matrix[i][j]=None
        def zeromatrix(matrix,n,m):
            for i in range(n):
                for j in range(m):
                    if matrix[i][j]==0:
                        markrow(matrix,n,m,i)
                        markcolumn(matrix,n,m,j)
            for i in range(n):
                for j in range(m):
                    if matrix[i][j] is None:
                        matrix[i][j]=0
            return matrix
        zeromatrix(matrix,n,m)