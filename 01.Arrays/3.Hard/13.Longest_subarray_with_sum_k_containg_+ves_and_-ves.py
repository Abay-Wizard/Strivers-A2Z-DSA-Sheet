# Given an array containing N integers and an integer K, 
# find the length of the longest subarray with the sum of the elements equal to K.


def longest_subarray_sum_k(nums,k): # brute force approach
    longest=0
    n=len(nums)
    for i in range(n):
        prefix_sum=0
        for j in range(i,n):
            prefix_sum+=nums[j]
            if prefix_sum==k:
                longest=max(longest,(j-i+1))
    return longest

# time complexity: O(n^2)
# space complexity: O(1)

def longest_subarray_optimal(nums,k):
    sum_index={}
    prefix_sum=0
    longest=0
    n=len(nums)
    for i in range(n):
        prefix_sum+=nums[i]
        target=prefix_sum-k
        if target in sum_index:
            longest=max(longest,i-sum_index[target])
        if prefix_sum not in sum_index:
            sum_index[prefix_sum]=i
    return longest
print(longest_subarray_optimal([10, 5, 2, 7, 1, 9],15))
            
    


                                          
    