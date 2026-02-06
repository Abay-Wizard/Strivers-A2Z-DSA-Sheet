# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
# For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
def findMin(nums):
    n=len(nums)
    low,high=0,n-1
    while low < high:
        mid=(low+high)//2
        if nums[mid] > nums[high]:
            low=mid+1
        else:
            high=mid
    return nums[low]