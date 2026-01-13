# Given an array with both positive and negative integers, 
# we need to compute the length of the largest subarray with a sum of 0.

def find_largest_subarray(nums):
    n=len(nums)
    largest=0
    for i in range(n):
        prefix_sum=0
        for j in range(i,n):
            prefix_sum+=nums[j]
            if prefix_sum ==0:
                largest=max(largest,j-i+1)
    return largest
#(find_largest_subarray([15, -2, 2, -8, 1, 7, 10, 23]))

# time complexity: O(n^2)
# space complexity: O(1)


def find_largest_subarray_optimal(nums):
    sum_index={0:-1}
    n=len(nums)
    largest=0
    prefix_sum=0
    for i in range(n):
        prefix_sum+=nums[i]
        if prefix_sum in sum_index:
            largest=max(largest,i-sum_index[prefix_sum])
        else:
            sum_index[prefix_sum]=i
    return largest
print(find_largest_subarray_optimal([15, -2, 2, -8, 1, 7, 10, 23]))
        