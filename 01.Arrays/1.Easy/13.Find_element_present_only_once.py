#QUESTION:-
#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#You must implement a solution with a linear runtime complexity and use only constant extra space.

# approach: Will be using Xor for optimal solution
import operator
def find_present_only_once(nums): # brute force
    count=dict()
    for i in nums:
        count[i]=count.get(i,0)+1
        
    for k in count:
        if count[k] ==1:
            return k
#print(find_present_only_once([1,3,3,4,4,1,9]))


def find_present_onlyonce(nums):
    xorx=0
    for num in nums:
        xorx=operator.xor(xorx,num)
    return xorx
print(find_present_onlyonce([1,3,3,4,4,1,9]))