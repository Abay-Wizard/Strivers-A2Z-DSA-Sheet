# problem: move zeros to the end of array
def move_zeros_to_end(arr):
    n=len(arr)
    k=-1
    for i in range(n):
        if arr[i]==0:
            k=i
            break
    if k==-1:
        return arr
    
    for j in range(k+1,n):
        if arr[j] !=0:
            arr[k],arr[j]=arr[j],arr[k]
            k+=1
    return arr
print(move_zeros_to_end([0,0,0,1,3,4,5]))