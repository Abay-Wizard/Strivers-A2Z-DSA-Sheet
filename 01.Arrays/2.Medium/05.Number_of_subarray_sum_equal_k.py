# QUESTION:
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# Example:
# Input: nums = [1,1,1], k = 2
# Output: 2

def find_number_of_subarrays_with_sumk(nums,k):
    n=len(nums)
    prefix_sum=0
    freq_sum={0:1}
    count=0
    for i in range(n):
        prefix_sum+=nums[i]
        target=prefix_sum-k
        if target in freq_sum:
          count+=freq_sum[target]
        freq_sum[prefix_sum] =freq_sum.get(prefix_sum,0)+1
    return count
print(find_number_of_subarrays_with_sumk([1,1,1],2))
