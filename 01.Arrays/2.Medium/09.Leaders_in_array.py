# Given an array A of positive integers. Your task is to find the leaders in the array. 
# An element of the array is a leader if it is greater than or equal to all the elements to its right side. 
# The rightmost element is always a leader.

def leaders_in_array(nums): # brute force approach
    leaders=[]
    n=len(nums)
    for i in range(n-1):
        isLeader=True
        for j in range(i+1,n):
            if nums[i] < nums[j]:
                isLeader=False
                break
        if isLeader:
            leaders.append(nums[i])
    leaders.append(nums[n-1])
    
    return leaders 

print(leaders_in_array([16,17,4,3,5,2]))

# time complexity: O(n^2)
# space complexity: O(n)


def leaders_in_array(nums): # optimal solution
    n=len(nums)
    maxi=nums[-1]
    leaders=[maxi]
    for i in range(n-1,-1,-1):
        if nums[i] > maxi:
            leaders.append(nums[i])
            maxi=nums[i]
    return leaders
print(leaders_in_array([16,17,4,3,5,2]))


# time complexity: O(n)
# space complexity: O(n)