# QUESTION:
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

#Example 1:
#Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
#Output: [[1,0,1],[0,0,0],[1,0,1]]

#Example 2:
#Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
#Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

def set_matrix_to_zeros(matrix,n,m): # brute force approach
    row=[0]*n
    col=[0]*m
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                row[i]=1
                col[j]=1
    
    for i in range(n):
        for j in range(m):
            if row[i]==1 or col[j]==1:
                matrix[i][j]=0
    return matrix
# print(set_matrix_to_zeros([[1,1,1],[1,0,1],[1,1,1]],3,3))

# time complextiy: O(2n*m)=>O(n*m)
# space complexity: O(n+m)

def set_matrix_to_zeros_optimal(matrix):
    n=len(matrix)
    m=len(matrix[0])
    first_row_zero=False
    first_col_zero=False
    for j in range(m):
        if matrix[0][j]==0:
            first_row_zero=True
    
    for i in range(n):
        if matrix[i][0]==0:
            first_col_zero=True
    
    for i in range(1,n):
        for j in range(1,m):
            if matrix[i][j]==0:
                matrix[0][j]=0
                matrix[i][0]=0
                
    for i in range(1,n):
        for j in range(1,m):
            if matrix[0][j]==0 or matrix[i][0]==0:
                matrix[i][j]=0
    
    if first_col_zero:
        for i in range(n):
            matrix[i][0]=0
            
    if first_row_zero:
        for j in range(m):
            matrix[0][j]=0
            
    return matrix
print(set_matrix_to_zeros_optimal([[1,1,1],[1,0,1],[1,1,1]]))

# time complexity: O(n*m)
# space complexity: O(1), I didn't use any extra space, I just did it in place