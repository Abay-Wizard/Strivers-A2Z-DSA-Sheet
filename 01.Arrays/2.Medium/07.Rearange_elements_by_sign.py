# problem: rearrange elements by sign


def rearrange_array_by_sign(nums): # brute force apprach
    n=len(nums)
    positive=[]
    negative=[]
    for i in range(n):
        if nums[i] > 0:
            positive.append(nums[i])
        elif nums[i] < 0:
            negative.append(nums[i])
    
    for i in range(n//2):
        nums[2*i]=positive[i]
        nums[2*i+1]=negative[i]
    return nums

# time complexity: O(2n)=>O(n)
# space complexity: O(n)

def rearrange_array_bysign(nums): # optimal solution
    n=len(nums)
    ans=[0]*n
    positive_idx=0
    negative_idx=1
    for i in range(n):
        if nums[i] < 0:
            ans[negative_idx]=nums[i]
            negative_idx+=2
        else:
            ans[positive_idx]=nums[i]
            positive_idx+=2
    return ans
print (rearrange_array_bysign([3,1,-2,-5,2,-4]))

# time complexity: O(n)
# space complexity: O(n)

# additional problem, if we are not sure that the number of negatives and positives are equal, return the last elements
# at the end of the array without altering their relative order

def rearrange_neg_pos_not_equal(nums):
    n=len(nums)
    positive=[]
    negative=[]
    ans=[0]*n
    for i in range(n):
        if nums[i] < 0:
            negative.append(nums[i])
        else:
            positive.append(nums[i])
    
    if len(negative) < len(positive):
        for i in range(len(negative)):
            ans[2*i]=positive[i]
            ans[2*i+1]=negative[i]
        index=2*len(negative)
        for i in range(len(negative),len(positive)):
            ans[index]=positive[i]
            index+=1
    else:
        for i in range(len(positive)):
            ans[2*i]=positive[i]
            ans[2*i+1]=negative[i]
        index=2*len(positive)
        for i in range(len(positive),len(negative)):
            ans[index]=nums[i]
            index+=1
    return ans
print(rearrange_neg_pos_not_equal([3,1,-2,-5,2,-4,8,9,10]))