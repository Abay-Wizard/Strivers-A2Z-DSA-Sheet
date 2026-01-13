# QUESTION:
# Given an array of integers. Find the Inversion Count in the array.

# Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. 
# If the array is already sorted then the inversion count is 0. 
# If an array is sorted in the reverse order then the inversion count is the maximum. 
# Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.


def count_inversions_brute(nums): # brute force approach 
    n=len(nums)
    count=0
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] > nums[j]:
                count+=1
    return count

# time complexity: O(n^2)
# space complexity: O(1)

def merge_sort(arr,low,high):
    count_inv=0
    if low < high:
        mid=(low+high)//2
        count_inv+= merge_sort(arr,low,mid)
        count_inv+= merge_sort(arr,mid+1,high)
        count_inv+= merge_and_count(arr,low,mid,high)
    return count_inv
                
def merge_and_count(arr,low,mid,high):
    left_half=arr[low:mid+1]
    right_half=arr[mid+1:high+1]
    i,j=0,0
    k=low
    swaps=0
   
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            arr[k]=left_half[i]
            i+=1
        else:
            arr[k]=right_half[j]
            swaps+=len(left_half)-i
            j+=1
        k+=1
    
    while i < len(left_half):
        arr[k]=left_half[i]
        i+=1
        k+=1
    while j < len(right_half):
        arr[k]=right_half[j]
        j+=1
        k+=1
    return swaps
        
def count_inversions(arr):
    return merge_sort(arr,0,len(arr)-1)
print(count_inversions([2, 4, 1, 3, 5]))

# time complexity: O(nlogn)
# space complexit: O(1)