# QUESTION:-
# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.



# Example 1:
# Input:  matrix = [[1,3,5,7]
#                 [10,11,16,20]
#                 [23,30,34,60]]
#         target = 3
# Output: true

def searchMatrix(matrix,target):
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n):
            if (matrix[i][0] <= target and matrix[i][m-1] >=target):
                return binary_search(matrix[i],target)
        return False
def binary_search(arr,target):
    n=len(arr)
    low,high=0,n-1
    while low <=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return True
        elif arr[mid] > target:
            high=mid-1
        else:
            low=mid+1
    return False

# time complexity: O(nlogm)
# space complexity: O(1)

def search_matrix_optimal(matrix,target):
    n,m=len(matrix),len(matrix[0])
    low,high=0,(n*m-1)
    while low <=high:
        mid=(low+high)//2
        row,col=mid//m,mid%m
        if matrix[row][col]==target:
            return True
        elif matrix[row][col] > target:
            high=mid-1
        else:
            low=mid+1
    return False

# time complexity: O(log(m*n))
# space complexity: O(1)