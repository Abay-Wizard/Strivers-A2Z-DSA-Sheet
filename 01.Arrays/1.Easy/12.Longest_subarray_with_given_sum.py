# Problem: find the longest subarray with sum k , the elements are all positive

def find_longest_subarray(nums,k): # this is brute force approach
    n=len(nums)
    length=0
    for i in range(n):
        for j in range(i,n):
            if sum(nums[i:j+1])==k:
                length=max(len(nums[i:j+1]),length)
    return length

#print(find_longest_subarray([2,0,0,3],3))
# time complexity: O(n^3)
# space complexity: O(1)


def find_longest_subarray(nums, k): # better solution 
    n = len(nums)
    max_len = 0
    for i in range(n):
        curr_sum=0
        for j in range(i,n):
            curr_sum+=nums[j]
            if curr_sum==k:
                max_len=max(max_len,j-i+1)
    

    return max_len

# time complexity: O(n^2)
# space complexity: O(1)

def find_longest_subarray(nums, k): # optimal
    prefix_sum = 0
    max_len = 0
    sum_index = {0: -1}  # prefix_sum : index
    n=len(nums)

    for i in range(n):
        prefix_sum+=nums[i]
        if prefix_sum-k in sum_index:
            max_len=max(max_len,i-sum_index[prefix_sum-k])
        else:
            if prefix_sum not in sum_index:
                sum_index[prefix_sum]=i
    return max_len
print(find_longest_subarray([1, 2, 3, 1, 1, 1, 1],3))

# time complexity: O(n)
# space complexity: O(1)