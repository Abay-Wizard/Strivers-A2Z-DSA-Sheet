# Given a sorted array arr[] of size N without duplicates, and given a value x. 
# Floor of x is defined as the largest element K in arr[] such that K is smaller than or equal to x. 
# Find the index of K (0-based indexing).

def Floor(nums,x):
    n=len(nums)
    low=0
    high=n-1
    index=-1
    while low <=high:
        mid=(low+high)//2
        if nums[mid] <=x:
            index=mid
            low=mid+1
        else:
            high=mid-1
    return index
print(Floor([1,2,8,10,11,12,19],5))
    
 