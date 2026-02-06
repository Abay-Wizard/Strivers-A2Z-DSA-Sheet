# You are given 2 numbers (n, m); the task is to find n√m (nth root of m).

# Example:

# Input: n = 2, m = 9
# Output: 3
# Explanation: 3^2 = 9

# Input: n = 3, m = 9
# Output: -1
# Explanation: 3rd root of 9 is not an integer.

def find_nth_root_of_m(n,m):
    low,high=0,m
    while low <=high:
        mid=(low+high)//2
        if mid**n==m:
            return mid
        elif mid**n < m:
            low=mid+1
        else:
            high=mid-1
    return -1
print(find_nth_root_of_m(2,9))