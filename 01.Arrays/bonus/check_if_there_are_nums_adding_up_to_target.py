# problem: check if there are elements whose sum is target in an array

def check_if_two_sum(nums,target): # brute force apprach
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j]==target:
                return True
                
    return False


def check_if_two_sum(nums,target): # better solution
    seen=set()
    for i in nums:
        diff=target-i
        if diff in seen:
            return True
        seen.add(i)
    return False

def check_if_there_are_two_sum(nums,target):# Greedy approach
    nums.sort()
    n=len(nums)
    left=0
    right=n-1
    while left < right:
        sum=nums[left]+nums[right]
        if sum==target:
            return True
        elif sum > target:
            right-=1
        else:
            left+=1
    return False

print(check_if_two_sum([1,3,0,6,3,6,3,7],10))