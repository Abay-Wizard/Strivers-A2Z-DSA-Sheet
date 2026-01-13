# Problem: Given a sorted array of intigers and target element, find the index of the target element

def binary_search(nums,target): # if low is greater than high, it means the element we are looking for is not in the array
    n=len(nums)
    low=0
    high=n-1
    for i in range(n):
        mid=(low+high)//2
        if nums[mid] ==target:
            return mid
        elif nums[mid] < target:
            low=mid+1
        else:
            high=mid-1
    if low <= high:
        return mid
    else:
        return -1

#print(binary_search([1,2,4,5,6,7,8,9,11],13))

