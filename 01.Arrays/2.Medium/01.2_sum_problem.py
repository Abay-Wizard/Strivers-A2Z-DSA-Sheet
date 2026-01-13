# problem: find the indices of two elements adding up to a target

def find_indices(nums,target):
    n=len(nums)
    seen=dict()
    for i in range(n):
       diff=target-nums[i]
       if diff in seen:
           return {i,seen[diff]}
       else:
           seen[nums[i]]=i

print(find_indices([2,7,11,15],9))

# time complexity: O(n)
# space complexity: O(n)