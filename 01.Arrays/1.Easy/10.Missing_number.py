# find a missing number from an array containing n distinct elements in range of [0,n]
def find_missing_number(nums): # this is brute force approach
    n=len(nums)
    for i in range(n+1):
        if not i in nums:
            return i
print(find_missing_number)
    