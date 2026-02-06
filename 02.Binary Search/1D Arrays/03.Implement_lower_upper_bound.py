# Given an unsorted array Arr[] of N integers and an integer X, find floor and ceiling of X in Arr[0..N-1].

# Floor of X is the largest element which is smaller than or equal to X. Floor of X doesn’t exist if X is smaller than the smallest element of Arr[].

# Ceil of X is the smallest element which is greater than or equal to X. Ceil of X doesn’t exist if X is greater than the greatest element of Arr[].

def floor_and_ceil(nums,x):
    nums.sort()
    floor=floor_idx(nums,x)
    ceil=ceil_idx(nums,x)
    return [floor,ceil]

def ceil_idx(nums,x):
    n=len(nums)
    low,high=0,n-1
    upper=-1
    while low <=high:
        mid=(low+high)//2
        if nums[mid] >=x:
            upper=nums[mid]
            high=mid-1
        else:
            low=mid+1
    return upper

def floor_idx(nums,x):
    n=len(nums)
    low,high=0,n-1
    lower=-1
    while low <=high:
        mid=(low+high)//2
        if nums[mid] <=x:
            lower=nums[mid]
            low=mid+1
        else:
            high=mid-1
    return lower
print(floor_and_ceil([5, 6, 8, 9, 6, 5, 5, 6],7))

