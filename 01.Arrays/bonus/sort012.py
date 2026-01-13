# problem: sort an array of 0's, 1's and 2's 

def sort_an_arrayof_012(arr): # brute force approach
    sorted_arr=[]
    zero_count=0
    one_count=0
    two_count=0
    for i in arr:
        if i==0:
            zero_count+=1
        elif i==1:
            one_count+=1
        else:
            two_count+=1
    
    for i in range(zero_count):
        sorted_arr.append(0)
    for j in range(one_count):
        sorted_arr.append(1)
    for k in range(two_count):
        sorted_arr.append(2)
    return sorted_arr
print(sort_an_arrayof_012([1,1,1,1,0,0,0,2,2,2,2,0,0,1]))

# time complexity: O(2n)
# space complexity: O(n)

def sort_an_arrayof_zeros_ones_and_twos(arr): # better solution
    n=len(arr)
    zero_count=0
    one_count=0
    two_count=0
    for i in arr:
        if i==0:
            zero_count+=1
        elif i==1:
            one_count+=1
        else:
            two_count+=1
    
    for i in range(zero_count):
        arr[i]=0
    for j in range(zero_count,zero_count+one_count):
        arr[j]=1
    for k in range(zero_count+one_count,n):
        arr[k]=2
    return arr

# time complexity: O(2n)
# space complexity: O(1)
# approach for the second is that every element from 0 to low-1 are zeros, and from low to mid-1 are ones and mid to high are unsorted!
def sort_array_of012(nums): # optimal => Dutch national flag algorithm
    n=len(nums)
    low=0
    mid=0
    high=n-1
    while mid < high:
        if nums[mid]==0:
            nums[low],nums[mid]=nums[mid],nums[low]
            low+=1
            mid+=1
        elif nums[mid]==1:
            mid+=1
        else:
            nums[mid],nums[high]=nums[high],nums[mid]
            high-=1
    return nums
print(sort_array_of012([0,2,2,2,1,1,1,0]))

# time complextiy: O(n)
# space complexity: O(1)
            

