# Question: Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized. Return the minimized largest sum of the split.

# Example:
# Input: nums = [7,2,5,10,8], k = 2
# Output: 18
# Explanation: There are four ways to split nums into two subarrays. The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.

def minMaxSubarraySum(nums,k):
    n=len(nums)
    if n < k:
        return -1
    low,high=max(nums),sum(nums)
    for i in range(low,high+1):
        if calculateNumberOfSubarrays(nums,i)==k:
            return i

def calculateNumberOfSubarrays(nums,subarray_sum):
    count_subarrays,temp_sum=1,0
    for num in nums:
        if temp_sum + num <=subarray_sum:
            temp_sum+=num
        else:
            count_subarrays+=1
            temp_sum=num
    return count_subarrays

# time complexity: O((high-low+1)*n)
# space complexity: O(1)

def minMaxSubarraySum(nums,k):
    n=len(nums)
    low,high=max(nums),sum(nums)
    while low <=high:
        mid=(low+high)//2
        if calculateNumberOfSubarrays(nums,mid) > k:
            low=mid+1
        else:
            high=mid-1
    return low

# time complexity: O(log(high-low)*n)
# space complexity: O(1)