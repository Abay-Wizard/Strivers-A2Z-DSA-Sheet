# QUESTION:
# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
# - Integers in each row are sorted in ascending order from left to right.
# - Integers in each column are sorted in ascending order from top to bottom.

# Example 1:
# Input: matrix = [
#   [1, 4, 7, 11, 15],
#   [2, 5, 8, 12, 19],
#   [3, 6, 9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ], target = 5
# Output: true
# Explanation: The element 5 is present in the matrix.

# Example 2:
# Input: matrix = [
#   [1, 4, 7, 11, 15],
#   [2, 5, 8, 12, 19],
#   [3, 6, 9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ], target = 20
# Output: false
# Explanation: The element 20 is not present in the matrix.

def searchMatrix(matrix, target):
    n,m=len(matrix),len(matrix[0])
    for i in range(n):
        index=-1
        if (matrix[i][0]<=target and matrix[i][m-1] >=target):
            index=binary_search(matrix[i],target)
            if index !=-1:
                return [i,index]
            else:
                continue
    return [-1,-1]
    
def binary_search(arr,target):
    n=len(arr)
    low,high=0,n-1
    while low <=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid] > target:
            high=mid-1
        else:
            low=mid+1
    return -1


# time complexity: O(nlogm)
# space complexity: O(1)

def searchMatrix_optimal(matrix,target):
    n,m=len(matrix),len(matrix[0])
    row,col=0,m-1
    while row < n and col >=0:
        if matrix[row][col]==target:
            return [row,col]
        elif matrix[row][col] < target:
            row+=1
        else:
            col-=1
    return [-1,-1]
print(searchMatrix_optimal( [
  [1, 4, 7, 11, 15],
  [2, 5, 8, 12, 19],
  [3, 6, 9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
],16))

# time complexity: O(log())
# space complexity: O(1)