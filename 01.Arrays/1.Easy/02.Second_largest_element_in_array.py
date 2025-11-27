# Given an array Arr of size N, print second largest distinct element from an array.
# for example input n=6, arr=[24,63,92,74,20,82] and output will be => 82

def find_2nd_largest(arr,n):
    Max=arr[0]
    for i in range(1,n):
        if arr[i] > Max:
            Max=arr[i]
    Sec_Max=None
    for i in arr:
        if i==Max:
            continue
        elif Sec_Max==None or Sec_Max <i:
            Sec_Max=i
    return Sec_Max
print(find_2nd_largest([-5,-5,3],3))
        
    