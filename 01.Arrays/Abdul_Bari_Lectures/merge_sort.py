# problem: Given unsorted array, sort it using mergeSort recursively

def merge_sort(arr,low,high):
    if low < high:
        mid=(low+high)//2
        merge_sort(arr,low,mid)
        merge_sort(arr,mid+1,high)
        merge(arr,low,mid,high)
    return arr
        
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

print(merge_sort([3,1,9,2,1,10],0,6))

# time complexity: O(nlogn) => dividing takes logn and merge takes n
# space complexity:O(n)