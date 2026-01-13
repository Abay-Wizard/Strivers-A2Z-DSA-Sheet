# problem: Given a matrix of n x n , rotate it by 90 degree
import numpy as np
def rotate_matrix_by_90(matrix): # this is brute force approach
    n=len(matrix)
    ans=np.zeros((n,n),dtype=int)
    for i in range(n):
        for j in range(n):
            ans[j][n-1-i]=matrix[i][j]
    
    
    return ans
#print(rotate_matrix_by_90([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))

# time complexity: O(n^2)
# space complextiy: O(n^2)

def rotate_matrix_optimal(matrix): # two steps, one => finding transpose, second => reverse the rows
    n=len(matrix)
    for i in range(n-1):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    
    for i in range(n):
        matrix[i].reverse()
        
    return matrix
print(rotate_matrix_optimal([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))

# time compelxity: O(n^2/2 + n) => O (n^2)=> b/c we are actually iterating over the upper half only
# space complexity: O(1)
    

