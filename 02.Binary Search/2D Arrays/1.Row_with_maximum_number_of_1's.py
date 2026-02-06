# QUESTION:-
# Given a boolean 2D array of n x m dimensions where each row is sorted. Find the 0-based index of the first row that has the maximum number of 1's.

# Example 1:

# Input:
# N = 4 , M = 4
# Arr[][] = {{0, 1, 1, 1},
#            {0, 0, 1, 1},
#            {1, 1, 1, 1},
#            {0, 0, 0, 0}}
# Output: 2
# Explanation: Row 2 contains 4 1's (0-based indexing).

def row_with_maxi_ones(matrix):
    n=len(matrix)
    m=len(matrix[0])
    ans_row=-1
    max_count=0
    for i in range(n):
        count_ones=0
        for j in range(m):
            if matrix[i][j]==1:
                count_ones+=1
        if count_ones >max_count:
            max_count=count_ones
            ans_row=i
    return ans_row


# time complexity: O(n*m)
# space complexity: O(1)

def lower_bound(arr,x):
    n=len(arr)
    low,high=0,n-1
    ans=n
    while low <=high:
        mid=(low+high)//2
        if arr[mid] >=x:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans

def row_with_maxi_ones_optimal(matrix):
    n=len(matrix)
    m=len(matrix[0])
    max_count=-1
    ans_row=-1
    for i in range(n):
        count_ones=m-lower_bound(matrix[i],1)
        if count_ones > max_count:
            max_count=count_ones
            ans_row=i
    return ans_row

#print(row_with_maxi_ones_optimal([[0, 1, 1, 1],[0,0,1,1],[1,1,1,1],[0,0,0,0]]))  

# time complexity: O(nlog(m))    
# space complexity: O(1)    
        
            
    