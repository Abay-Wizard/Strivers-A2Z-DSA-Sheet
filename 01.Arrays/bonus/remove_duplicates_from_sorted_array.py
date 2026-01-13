# problem: remove duplicates from sorted array, return only the number of unique elements in the array

def remove_duplicates_form_sorted_array(arr):
    n=len(arr)
    k=0
    for j in range(1,n):
        if arr[j] !=arr[k]:
            k+=1
            arr[k],arr[j]=arr[j],arr[k]
    return k+1,arr[:k+1]
print(remove_duplicates_form_sorted_array([1,1,2,2,3,3,4,4,5,5]))