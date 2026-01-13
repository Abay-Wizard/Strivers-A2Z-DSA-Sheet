# problem: Given an array, find the number of subarrays whose sum is k

def count_subarrays_sum_k(nums,k): # this is brute force approach
    n=len(nums)
    count=0
    for i in range(n):
        for j in range(i,n):
            if sum(nums[i:j+1])==k:
                count+=1
    return count

# time complexity: O(n^3)
# space complexity: O(1)

#print(count_subarrays_sum_k([1,2,3,-3,1,1,1,4,2,-3],3))

def count_subarrays_k_sum(nums,k): # this is better solution
    n=len(nums)
    count=0
    for i in range(n):
        curr_sum=0
        for j in range(i,n):
            curr_sum+=nums[j]
            if curr_sum==k:
                count+=1
    return count

# time complexity: O(n^2)
# space complexity: O(1)

#print(count_subarrays_k_sum([1,2,3,-3,1,1,1,4,2,-3],3))

def count_subarrays_sumk(nums,k):
   n=len(nums)
   sum_freq={0:1}
   prefix_sum=0
   total_count=0
   for num in nums:
       prefix_sum+=num
       target=prefix_sum-k
       if target in sum_freq:
           total_count+=sum_freq[target]
       sum_freq[prefix_sum]=sum_freq.get(prefix_sum,0)+1
       
   return total_count
              
# time complexity: O(n)
# space complexity: O(n) 
    
print(count_subarrays_sumk([1,2,3,-3,1,1,1,4,2,-3],3))