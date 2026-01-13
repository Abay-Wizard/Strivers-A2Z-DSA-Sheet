# QUESTION:
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# - 0 <= a, b, c, d < n
# - a, b, c, and d are distinct.
# - nums[a] + nums[b] + nums[c] + nums[d] == target

# Example:
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

def unique_quadraplets_sum_target(nums,target):
    n=len(nums)
    nums.sort()
    final_list=[]
    for i in range(n):
        if i > 0 and nums[i]==nums[i-1]:
            continue
        for j in range(i+1,n):
            if nums[j]==nums[j-1]:
                continue
            k=j+1
            l=n-1
            while k < l:
                four_sum=nums[i]+nums[j]+nums[k]+nums[l]
                if four_sum < target:
                    k+=1
                elif four_sum > target:
                    l-=1
                else:
                    temp=[nums[i],nums[j],nums[k],nums[l]]
                    final_list.append(temp)
                    k+=1
                    l-=1
                    while k < l and nums[k]==nums[k-1]:
                        k+=1
                    while k < l and nums[l] ==nums[l+1]:
                        l-=1
    return final_list
print(unique_quadraplets_sum_target([1,0,-1,0,-2,2],0))
            