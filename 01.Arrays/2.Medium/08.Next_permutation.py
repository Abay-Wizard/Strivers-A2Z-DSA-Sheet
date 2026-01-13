# Given, an array of numbers, find the next permutation

def next_permutation(nums):
    n=len(nums)
    index=-1
    for i in range(n-2,-1,-1): # this is to find the breaking point where we start rearranging elements
        if nums[i] < nums[i+1]:
            index=i
            break
    
    if index ==-1: 
        nums.reverse()
        return nums
        
    for i in range(n-1,index,-1): 
        if nums[i] > nums[index]:
            nums[i],nums[index]=nums[index],nums[i]
            break
    
    nums[index+1:]=reversed(nums[index+1:])
    
    return nums


# time complexity: O(2n) => O(n)
# space complexity: O(1)



def next_permutation(nums):
    n=len(nums)
    index=-1
    for i in range(n-2,-1,-1):
        if nums[i] < nums[i+1]:
            index=i
            break
    if index ==-1:
        nums.reverse()
        return nums
    
    for i in range(n-1,index,-1):
        if nums[i] > nums[index]:
            nums[i],nums[index]=nums[index],nums[i]
            break
    nums[index+1:]=reversed(nums[index+1:])
    
    return nums
print(next_permutation([3,2,1]))