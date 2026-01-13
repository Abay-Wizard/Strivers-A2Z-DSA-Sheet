# QUESTION:
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Example:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

def find_triplets(nums): # brute force approach
    trip_set=set()
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if nums[i]+nums[j]+nums[k] ==0:
                    temp=sorted([nums[i],nums[j],nums[k]])
                    trip_set.add(tuple(temp))
    return [list(t) for t in trip_set]


# time complexity: O(n^3)
# space complexity: O(n^2)

def find_triplets_better(nums): # better solution
    trip_set=set()
    n=len(nums)
    for i in range(n):
        temp_set=set()
        for j in range(i+1,n):
            k=-(nums[i]+nums[j])
            if k in temp_set:
                temp=sorted([nums[i],nums[j],k])
                trip_set.add(tuple(temp))
            temp_set.add(nums[j])
    return [list(t) for t in trip_set]

# time complexity: O(n^2)
# space complexity: O(n)

def find_triplets_optimal(nums):
    nums.sort()
    trip_list=[]
    n=len(nums)
    for i in range(n):
        j=i+1
        k=n-1
        if (i > 0 and nums[i]==nums[i-1]):
            continue
        while j < k:
            sum=nums[i]+nums[j]+nums[k]
            if sum < 0:
                j+=1
            elif sum > 0:
                k-=1
            else:
                temp=[nums[i],nums[j],nums[k]]
                trip_list.append(temp)
                j+=1
                k-=1
                while (j < k and nums[k-1]==nums[k]):
                    k-=1
                while (j < k and nums[j]==nums[j-1]):
                    j+=1
    return trip_list
print(find_triplets_optimal([-1,0,1,2,-1,-4]))

# time complexity: O(n^2)
# space complexity: O(m) where m is the number of triplets 