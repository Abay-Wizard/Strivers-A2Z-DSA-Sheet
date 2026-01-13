# problem: Given an array, find the element that occurs more than n/2 where n is the length of the array

def majority_element(nums): # brute force approach
    n=len(nums)
    counts=dict()
    for num in nums:
        counts[num]=counts.get(num,0)+1
    for k in counts:
        if counts[k] > (n//2):
            return k


# time complexity: O(2n)=>O(n)
# space complexity: O(n)

def majority_element(nums): # Moore's voting algorithm (optimal solution)
    el=nums[0]
    count=1
    n=len(nums)
    for i in range(1,n):
        if count==0:
            el=nums[i]
            count+=1
        elif nums[i]==el:
            count+=1
        else:
            count-=1
    
    return el
print(majority_element([1,1,0,0,0,0,9]))
    
# time complexity: O(2n)=>O(n) b/c we are doing two over passes!
# space complexity: O(1)