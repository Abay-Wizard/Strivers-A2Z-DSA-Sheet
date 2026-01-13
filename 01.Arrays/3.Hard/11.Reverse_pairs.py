# QUESTION:
# Given an integer array nums, return the number of reverse pairs in the array.
# A reverse pair is a pair (i, j) where:
# 0 <= i < j < nums.length and
# nums[i] > 2 * nums[j].




def merge_sort(arr,low,high):
    count_rev=0
    if low < high:
        mid=(low+high)//2
        count_rev+= merge_sort(arr,low,mid)
        count_rev+=merge_sort(arr,mid+1,high)
        count_rev+=count_pairs(arr,low,mid,high)
        merge(arr,low,mid,high)
    return count_rev
    
def count_pairs(arr,low,mid,high):
    pairs=0
    right=mid+1
    for left in range(low,mid+1):
        while right <= high and arr[left] > 2*arr[right]:
            right+=1
        pairs+=right-(mid+1)
    return pairs


        
def merge(arr,low,mid,high):
    left_half=arr[low:mid+1]
    right_half=arr[mid+1:high+1]
    i=0
    j=0
    k=low
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k]=left_half[i]
            i+=1
        else:
            arr[k]=right_half[j]
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
def reverse_pairs(arr):
    return merge_sort(arr,0,len(arr)-1)
print(reverse_pairs([1,3,2,3,1]))