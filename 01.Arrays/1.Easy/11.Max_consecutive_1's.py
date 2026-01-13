# problem: Given an array, find maximum length of consecutive 1's
def max_consecutive_ones(arr):
    count=0
    n=len(arr)
    maxL=0
    for i in range(n):
        if arr[i]==1:
            count+=1
            if count > maxL:
                maxL=count
        else:
            count=0
    return maxL
print(max_consecutive_ones([1,1,0,1,1,1,1,9,9,1,1,1]))