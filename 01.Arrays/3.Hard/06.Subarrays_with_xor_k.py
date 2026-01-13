# Given an array 'A' consisting of 'N' integers and an integer 'B', find the number of subarrays of array 'A' whose bitwise XOR of all elements is equal to 'B'.

# Example:
# Input: 'N' = 4, 'B' = 2
# 'A' = [1, 2, 3, 2]
# Output: 3
def count_subarrays_xor_as_k(nums,k): # brute force approach
    n=len(nums)
    count=0
    for i in range(n):
        for j in range(i,n):
            final_xor=0
            for num in nums[i:j+1]:
                final_xor=final_xor^num
            if final_xor==k:
                count+=1
    return count
#print(count_subarrays_xor_as_k([4,2,2,6,4],6))

# time complexity: O(n^3)
# space complexity: O(1)

def count_subarrays_better(nums,k):
    n=len(nums)
    count=0
    for i in range(n):
        final_xor=0
        for j in range(i,n):
            final_xor=final_xor^nums[j]
            if final_xor==k:
                count+=1
    return count
#print(count_subarrays_better([4,2,2,6,4],6))


# time complexity: O(n^2)
# space complexity: O(1)

def count_subarrays_optimal(nums,k):
    xorCount={0:1}
    prefix_xor=0
    count=0
    n=len(nums)
    for i in range(n):
        prefix_xor=prefix_xor^nums[i]
        if prefix_xor^k in xorCount:
            count+=xorCount[prefix_xor^k] 
        xorCount[prefix_xor]=xorCount.get(prefix_xor,0)+1
    return count
#print(count_subarrays_optimal([4,2,2,6,4],6))

# time complexity: O(n)
# space complexit: O(n) => I traded space for faster time 


def isAlphabeticPalindrome(code):
    alpha_code=''
    for char in code:
        if char.isalpha():
            alpha_code+=char
    print(alpha_code)
    n=len(alpha_code)
    i,j=0,n-1
    while i <= j:
        if alpha_code[i].lower() == alpha_code[j].lower():
            i+=1
            j-=1
        else:
            return 0
    return 1
print(isAlphabeticPalindrome('abc123cba'))




