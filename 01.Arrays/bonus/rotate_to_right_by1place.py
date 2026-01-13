# problem: rotate array to right by one place
def rotate_array_to_right_b1place(arr):
    n=len(arr)
    k=-1
    for j in range(-2,-n-1,-1):
        arr[k],arr[j]=arr[j],arr[k]
        k-=1
    return arr
print(rotate_array_to_right_b1place([1,2,3,4,5]))