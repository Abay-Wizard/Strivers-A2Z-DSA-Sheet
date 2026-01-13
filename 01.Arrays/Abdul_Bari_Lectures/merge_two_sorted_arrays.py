# Problem: Given two sorted arrays, merge them without using extra space

def merge_2sorted_arrays_without_space(arr1,arr2):
    n=len(arr1)
    m=len(arr2)
    i=n-1
    j=0
    while i >=0 and j < m:
        if arr1[i] >arr2[j]:
            arr1[i],arr2[j]=arr2[j],arr1[i]
            i-=1
            j+=1
        else:
            break
    arr1.sort()
    arr2.sort()
    print(arr1,arr2)
    
#merge_2sorted_arrays_without_space([1,2,4,7],[0,3,8,9])

def merge_2sorted_arrays_without_s(arr1,arr2):
    n=len(arr1)
    m=len(arr2)
    length=n+m
    gap=(length//2 + length % 2)
    while gap > 0:
        left=0
        right=left+gap
        while right < length:
            if left < n and right >=n:
                merge_sort(arr1,left,arr2,right-n)
            elif left >=n:
                merge_sort(arr2,left-n,arr2,right-n)
            else:
                merge_sort(arr1,left,arr1,right)
            left+=1
            right+=1
        if gap==1:
            break
        gap=(gap//2)+(gap % 2)
        
    print(arr1,arr2)



def merge_sort(arr1,idx1,arr2,idx2):
    if arr1[idx1] > arr2[idx2]:
        arr1[idx1],arr2[idx2]=arr2[idx2],arr1[idx1]
        
merge_2sorted_arrays_without_s([1,2,4,7],[0,3,8,9])