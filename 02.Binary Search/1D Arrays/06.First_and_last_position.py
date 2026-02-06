# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

# lower_bound is the smallest number greater or equal to target

# upper_bound is the smallest number strictly greater than target

def find_first_last_position(nums,target):
    if check_if_exists(nums,target):
        last_pos=upper_bound_idx(nums,target)
        first_pos=lower_bound_idx(nums,target)
        return [first_pos,last_pos-1]
    else:
        return [-1,-1]
        
def check_if_exists(nums,target):
    n=len(nums)
    low,high=0,n-1
    while low <=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return True
        elif nums[mid] < target:
            low=mid+1
        else:
            high=mid-1
    return False
    
def lower_bound_idx(nums,target):
    n=len(nums)
    low,high=0,n-1
    lower_idx=n
    while low <=high:
        mid=(low+high)//2
        if nums[mid] >=target:
            lower_idx=mid
            high=mid-1
        else:
            low=mid+1
    return lower_idx

def upper_bound_idx(nums,target):
    n=len(nums)
    low,high=0,n-1
    upper_idx=n
    while low <=high:
        mid=(low+high)//2
        if nums[mid] > target:
            upper_idx=mid
            high=mid-1
        else:
            low=mid+1
    return upper_idx
print(find_first_last_position([5,7,7,8,8,10],8))
    