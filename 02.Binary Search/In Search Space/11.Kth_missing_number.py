# Question: Given a sorted array arr of positive integers and an integer k, find the kth positive integer that is missing from the array.

# Example:
# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

def missing_number(arr,k): # brute force approach
    for i in arr:
        if i <=k:
            k+=1
        else:
            break
    return k

# time complexity: O(n)
# space complexity: O(1)


def missing_number_optimal(arr,k):
    low,high=0,len(arr)-1
    while low <=high:
        mid=(low+high)//2
        missing=arr[mid]-mid+1
        if missing < k:
            low=mid+1
        else:
            high=mid-1
    return low+k

# time complexity: O(log(n))
# space complexity: O(1)


