# problem: sort an array of 0's, 1's, and 2's 
# assumption: all elements from 0 to low-1 are zeros, low to mid-1 are ones, and mid to high are unsorted
# this is Dutch national flag theorem
def sort_arrayof012(nums):
    n=len(nums)
    low=0
    mid=0
    high=n-1
    while mid < high:
        if nums[mid] ==0:
            nums[low],nums[mid]=nums[mid],nums[low]
            low+=1
            mid+=1
        elif nums[mid] ==1:
            mid+=1
        else:
            nums[mid],nums[high]=nums[high],nums[mid]
            high-=1
    return nums
print(sort_arrayof012([0,2,2,2,1,1,1,0]))

# time complexity: O(n)
# space complexity: O(1)
    