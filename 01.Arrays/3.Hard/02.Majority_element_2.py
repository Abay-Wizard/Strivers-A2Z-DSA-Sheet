# QUESTION:
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# Example 1:
# Input: nums = [3,2,3]
# Output: [3]

def majority_element2(nums): # brute force approach
    final_list=[]
    n=len(nums)
    for i in range(n):
        count=0
        for j in range(n):
            if nums[i]==nums[j]:
                count+=1
        if count > (n//3) and nums[i] not in final_list:
            final_list.append(nums[i])
    return final_list

# time complexity: O(n^2)
# space complexity: O(1)

def majority_element2_better(nums): # better solution, I traded space for faster time
    count=dict()
    n=len(nums)
    final_list=[]
    for num in nums:
        count[num]=count.get(num,0)+1
    for num in count:
        if count[num] > (n//3):
            final_list.append(num)
    return final_list

# time complexity: O(n)
# space complexity: O(n) 
    
def majority_element2_optimal(nums):
    n=len(nums)
    count1,count2=0,0
    el1,el2 =None,None
    for i in range(n):
        if count1==0 and nums[i] !=el2:
            count1+=1
            el1=nums[i]
        elif count2==0 and nums[i] !=el1:
            count2+=1
            el2=nums[i]
        elif el1 ==nums[i]:
            count1+=1
        elif el2==nums[i]:
            count2+=1
        else:
            count1-=1
            count2-=1
    final_list=[]
    c1,c2=0,0
    for i in range(n):
        if nums[i]==el1:
            c1+=1
        if nums[i]==el2:
            c2+=1
    if c1 > (n//3):
        final_list.append(el1)
    if c2 > (n//3):
        final_list.append(el2)
    return final_list

# time complexity: O(n)
# space complexity: O(1)