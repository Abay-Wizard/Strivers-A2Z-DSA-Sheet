# Question:
# You are given an array of integers nums and an integer threshold. We need to find the smallest divisor
# such that the result of dividing each element of the array by the divisor and summing up the results
# is less than or equal to the threshold.

# Example:
# Input: nums = [1,2,5,9], threshold = 6
# Output: 5
# Explanation: We can get a sum of 17 (1+2+5+9) if the divisor is 1.
# If the divisor is 4, we can get a sum of 7 (1+1+2+3).
# If the divisor is 5, the sum will be 5 (1+1+1+2).
# The smallest divisor that gives a sum less than or equal to the threshold is 5.
import math
def find_smallest(nums,threshold):
    low,high=1,max(nums)
    ans=None
    while low <=high:
        mid=(low+high)//2
        if find_sum(mid,nums) <=threshold:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans

def find_sum(d,nums):
    total_sum=0
    for i in nums:
        total_sum+=math.ceil(i/d)
    return total_sum

print(find_smallest([1,2,5,9],6))