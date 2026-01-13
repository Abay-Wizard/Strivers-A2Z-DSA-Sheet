# problem: Given an array, find the subarray with the largest product

def largest_product_subarray(nums): # brute force approach
    largest=-1
    n=len(nums)
    for i in range(n):
        temp_prod=1
        for j in range(i,n):
            temp_prod*=nums[j]
            largest=max(largest,temp_prod)
    return largest
print(largest_product_subarray([2,3,-2,4]))

# time complexity: O(n^2)
# space complexity: O(1)


def maximum_product(nums):
    n=len(nums)
    temp_prod=1
    maxi=min(nums)
    for i in range(n):
        temp_prod*=nums[i]
        maxi=max(maxi,temp_prod)
        if temp_prod==0:
            temp_prod=1
    temp_prod=1
    for i in range(n-1,-1,-1):
        temp_prod*=nums[i]
        maxi=max(maxi,temp_prod)
        if temp_prod==0:
            temp_prod=1
    return maxi
# time complexity: O(nlogn)
# space complexity: O(1)
        