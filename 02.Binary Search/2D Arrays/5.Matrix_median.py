# Given a row-wise sorted matrix of size R*C where R and C are always odd, find the median of the matrix.

# Example:

# Input:
# R = 3, C = 3
# M = [[1, 3, 5], 
#      [2, 6, 9], 
#      [3, 6, 9]]
# Output: 5
# Explanation: Sorting matrix elements gives us {1, 2, 3, 3, 5, 6, 6, 9, 9}. Hence, 5 is the median. 
def matrix_median(matrix):
    final_list=[]
    n,m=len(matrix),len(matrix[0])
    for i in range(n):
        for j in range(m):
            final_list.append(matrix[i][j])
    final_list.sort()
    return final_list[m*n//2]


# time complexity: O(n*m + n*mlog(m*n))=>O(n*mlog(n*m))
# space complexity: O(n*m)

def matrix_median_optimal(matrix):
    n,m=len(matrix),len(matrix[0])
    low,high=float('inf'),float('-inf')
    for i in range(n):
        low=min(low,matrix[i][0])
        high=max(high,matrix[i][m-1])
    req=n*m//2
    while low <=high:
        mid=(low+high)//2
        smallEquals=countSmallEquals(matrix,mid)
        if smallEquals <=req:
            low=mid+1
        else:
            high=mid-1
    return low

def countSmallEquals(matrix,num):
    n,m=len(matrix),len(matrix[0])
    count=0
    for i in range(n):
        count+=upper_bound(matrix[i],num)
    return count

def upper_bound(arr,x):
    m=len(arr)
    low,high=0,m-1
    ans=m
    while low <=high:
        mid=(low+high)//2
        if arr[mid] > x:
            high=mid-1
            ans=mid
        else:
            low=mid+1
    return ans
        
print(matrix_median_optimal([[1, 3, 5], 
    [2, 6, 9], 
    [3, 6, 9]]))

# time complexity: O(log(high-low)*nlog(m))
# space complexity: O(1)
        