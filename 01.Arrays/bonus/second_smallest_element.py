def find_2nd_smallest(arr):
    smallest=arr[0]
    n=len(arr)
    for i in range(1,n):
        if arr[i] < smallest:
            smallest=arr[i]
    sec_smallest=None
    for i in arr:
        if (sec_smallest is None or (i < sec_smallest and i !=smallest)):
            sec_smallest=i
    return sec_smallest
#print(find_2nd_smallest([2,2,1,4,6,3,7]))
# time complexity: O(2n) => b/c we are doing two passes

def get_2nd_smallest(arr,n):
    smallest=arr[0]
    ssmallest=None
    for i in range(1,n):
        if arr[i] < smallest:
            ssmallest=smallest
            smallest=arr[i]
        elif ssmallest is None or (arr[i] < ssmallest and arr[i] !=smallest):
            ssmallest=arr[i]
    return ssmallest
print(get_2nd_smallest([2,2,1,4,6,3,7],7))
    
    