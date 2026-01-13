'''
QUESTION:-

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

APPROACH:-
To rotate the array k places to right follow below steps
-> Reverse first n-k elements
-> Reverse last k elements
-> Reverse the entire array

To rotate the array k places to left follow below steps
-> Reverse first k elements
-> Reverse last n-k elements
-> Reverse the entire array


'''

def rotate_right(arr,k):
    n=len(arr)
    k=k%n
    arr[:n-k]=reversed(arr[:n-k])
    arr[n-k:]=reversed(arr[n-k:])
    arr[:]=reversed(arr[:])
    return arr
   
#print(rotateRight([1,2,3,4,5,6,7],3))
    
    
def rotate_left(arr,k):
    n=len(arr)
    k=k%n
    arr[:k]=reversed(arr[:k])
    arr[k:]=reversed(arr[k:])
    arr[:]=reversed(arr[:])
    #print(arr)
rotate_left([1,2,3,4,5,6,7],1)
    
    
    
    
    
    

def rotate_array_byN_place(nums,N): # to right
    n=len(nums)
    N=N%n
    for i in range(N):
        k=-1
        for j in range(-2,-(len(nums)+1),-1):
            nums[j],nums[k]=nums[k],nums[j]
            k-=1
    return nums
#print(rotate_array_byN_place([1,2,3,4,5,6,7],3))

def rotate_toleft_byk_place(arr,k):
    n=len(arr)
    k=k%n
    temp=arr[:k]
    for i in range(k,n):
        arr[i-k]=arr[i]
    arr[n-k:]=temp
    return arr
#print(rotate_toleft_byk_place([1,2,3,4,5,6,7],3))


def rotate_toright_byk_place(arr,k):
    n=len(arr)
    k=k%n
    return arr[n-k:] + arr[:n-k]
print(rotate_toright_byk_place([1,2,3,4,5,6,7],3))
    