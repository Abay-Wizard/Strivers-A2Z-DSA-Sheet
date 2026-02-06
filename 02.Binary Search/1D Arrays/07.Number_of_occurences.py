# Given a sorted array Arr of size N and a number X, you need to find the number of occurrences of X in Arr.

def find_number_of_occurence(nums,target):
    count=0
    last_pos=upper_bound_idx(nums,target)
    first_pos=lower_bound_idx(nums,target)
    count=last_pos-first_pos
    return count
        
    
def lower_bound_idx(nums,target):
    n=len(nums)
    low,high=0,n-1
    lower_idx=-1
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
    upper_idx=len(nums)
    while low <=high:
        mid=(low+high)//2
        if nums[mid] > target:
            upper_idx=mid
            high=mid-1
        else:
            low=mid+1
    return upper_idx
print(find_number_of_occurence([5,7,7,8,8,10],5))
    