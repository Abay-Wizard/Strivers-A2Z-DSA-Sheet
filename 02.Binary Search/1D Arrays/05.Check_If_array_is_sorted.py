# Given an array arr[] of size N, check if it is sorted in non-decreasing order or not.

def check_if_sorted(nums,low,high):
    if low >=high:
        return True
    mid =(low+high)//2
    if nums[mid] <=nums[mid+1] and (check_if_sorted(nums,low,mid) and check_if_sorted(nums,mid+1,high)):
        return True
    else:
        return False
arr=[10, 20, 30, 40, 50]
print(check_if_sorted(arr,0,len(arr)-1))