# Given an array of integers nums which is sorted in ascending order, 
# and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.

def find_target(nums,target): # this is iterative
    n=len(nums)
    low=0
    high=n-1
    while low <=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid] > target:
            high=mid-1
        else:
            low=mid+1
    return -1


def find_target_rec(nums,low,high,target): # recursive approach
    if low > high:
        return -1
    mid = (low+high)//2
    if nums[mid]==target:
        return mid
    elif nums[mid] < target:
        return find_target_rec(nums,mid+1,high,target)
    else:
        return find_target_rec(nums,low,mid-1,target)
print(find_target_rec([-1,0,3,5,9,12],0,6,9))

        
