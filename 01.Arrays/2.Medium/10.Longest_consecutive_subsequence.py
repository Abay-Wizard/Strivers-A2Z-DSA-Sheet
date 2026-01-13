# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

def longest_consecutive_subsquence(nums): # this is better solution
    n=len(nums)
    nums.sort()
    longest=1
    lastSeen=nums[0]
    tempCount=1
    for i in range(1,n):
        if nums[i] == lastSeen:
            continue
        elif nums[i]-lastSeen > 1:
            lastSeen=nums[i]
        else:
            tempCount+=1
            lastSeen+=1
        longest=max(longest,tempCount)
        
    return longest
print(longest_consecutive_subsquence([0,3,7,2,5,8,4,6,0,1]))

# time complexity: O(nlogn + n)=>O(nlogn)
# space complexity: O(1)


def longest_cons_subsequence(nums):
    nums_set=set(nums)
    n=len(nums)
    longest=0
    for num in nums_set:
        if not num-1 in nums_set:
            tempCount=1
            lastSeen=num
            while lastSeen+1 in nums_set:
                tempCount+=1
                lastSeen+=1
            longest=max(longest,tempCount)
    
    return longest

#print(longest_cons_subsequence([0,3,7,2,5,8,4,6,0,1]))
        
        
            