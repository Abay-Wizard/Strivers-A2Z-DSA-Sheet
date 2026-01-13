# QUESTION:-

# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

def spiral_matrix(matrix): # the direction we follow is right => bottom => left => top
    n=len(matrix)
    m=len(matrix[0])
    ans=[]
    left=0
    right=m-1
    top=0
    bottom=n-1
    while left <= right and top <= bottom:
        for i in range(left,right+1):
            ans.append(matrix[top][i])
        top+=1
        
        for i in range(top,bottom+1):
            ans.append(matrix[i][right])
        right-=1
        if top <=bottom:
            for i in range(right,left-1,-1):
                ans.append(matrix[bottom][i])
            bottom-=1
        
        if left <=right:
            for i in range(bottom,top-1,-1):
                ans.append(matrix[i][left])
            left+=1
    
    return ans
print(spiral_matrix( [[1,2,3],[4,5,6],[7,8,9]]))

# time complexity: O(n*m)
# space complexity: O(n*m)
    