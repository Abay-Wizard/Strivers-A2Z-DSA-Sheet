# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

def search_insert(nums,target):
    n=len(nums)
    low,high=0,n-1
    idx=-1
    while low <=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid] < target:
            idx=mid
            low=mid+1
        else:
            high=mid-1
    return idx+1
print(search_insert([1,3,5,6],2))
            