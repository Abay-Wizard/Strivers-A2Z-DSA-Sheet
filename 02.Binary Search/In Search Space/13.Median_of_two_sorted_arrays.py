# Given two sorted arrays nums1 and nums2 of sizes m and n respectively, 
# you need to find the median of the two sorted arrays.

def median_of_sorted_arrays(arr1,arr2):
    median=0
    merged_arr=merge_sort(arr1,arr2)
    n=len(merged_arr)
    if n % 2==0:
        median =(merged_arr[n//2]+merged_arr[n//2-1])/2
    else:
        median=merged_arr[n//2]
    return median
def merge_sort(arr1,arr2):
    final_arr=[]
    m=len(arr1)
    n=len(arr2)
    i,j=0,0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            final_arr.append(arr1[i])
            i+=1
        else:
            final_arr.append(arr2[j])
            j+=1
    while i < m:
        final_arr.append(arr1[i])
        i+=1
    while j < n:
        final_arr.append(arr2[j])
        j+=1
    return final_arr


# time complexity: O(n+m)
# space complexity: O(n+m)

def median_of_sorted_arrays_optimal(arr1,arr2):
    if len(arr1) > len(arr2):
        arr1,arr2=arr2,arr1
    n1,n2=len(arr1),len(arr2)
    n=n1+n2
    left=(n+1)//2
    low,high=0,n1
    while low <= high:
        L1,L2=float('-inf'),float('-inf')
        r1,r2=float('inf'),float('inf')
        mid1=(low+high)//2
        mid2=left-mid1
        if mid1 < n1:
            r1=arr1[mid1]
        if mid2 < n2:
            r2=arr2[mid2]
        if (mid1-1) >=0:
            L1=arr1[mid1-1]
        if (mid2-1) >=0:
            L2=arr2[mid2-1]
        if (L1 <= r2 and L2 <=r1):
            if n%2==0:
                return (max(L1,L2)+min(r1,r2))/2
            else:
                return max(L1,L2)
        elif L1 > r2:
            high=mid1-1
        else:
            low=mid1+1
print(median_of_sorted_arrays_optimal([1,2,5,9],[1,2,3,3]))

# time complexity: O(log(min(n1,n2)))
# space complexity: O(1)
        

