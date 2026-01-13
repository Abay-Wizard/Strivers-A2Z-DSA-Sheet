# problem: Given an array, find the subarray with largest sum

def max_subarray(nums): # brute force approach
    n=len(nums)
    max_sum=nums[0]
    for i in range(n):
        prefix_sum=0
        for j in range(i,n):
            prefix_sum+=nums[j]
            max_sum=max(max_sum,prefix_sum)
    return max_sum
#print(max_subarray([1,2,4,0,-1,-8,9,-22]))

# time complextiy: O(n^2)
# space complexity: O(1)


def max_subarray_kadane(nums): # most optimal solution => Kadane's algorithm
    n=len(nums)
    max_sum=nums[0]
    curr_sum=nums[0]
    for i in range(1,n):
        curr_sum+=nums[i]
        max_sum=max(max_sum,curr_sum)  
        if curr_sum < 0:
            curr_sum=0
    return max_sum
print(max_subarray_kadane([1,2,4,0,-1,-8,9,2]))

# time complexity: O(n)
# space complexity: O(1)
