# You are given a sorted array consisting of only integers where every element appears exactly twice, 
# except for one element which appears exactly once.

# Return the single element that appears only once.

def find_single_element(nums):
    n=len(nums)
    low,high=0,n-1
    while low < high:
        mid=(low+high)//2
        if mid % 2==0:
           if nums[mid] ==nums[mid+1]:
               low=mid+1
           else:
               high=mid
        else:
            if nums[mid] !=nums[mid+1]:
                low=mid+1
            else:
                high=mid
    return nums[low]
print(find_single_element([3,4,4,5,5]))