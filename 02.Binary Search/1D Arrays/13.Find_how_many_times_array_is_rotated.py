# Given an ascending sorted rotated array Arr of distinct integers of size N. 
# The array is right rotated K times. Find the value of K.


def find_number_of_rotation(nums):
    n=len(nums)
    low,high=0,n-1
    while low < high:
        mid=(low+high)//2
        if nums[mid] > nums[high]:
            low=mid+1
        else:
            high=mid
    return low
print(find_number_of_rotation([5, 1, 2, 3, 4]))
