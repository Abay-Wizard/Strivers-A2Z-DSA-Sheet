# problem: given an array of size (n), check if it is sorted or not
def check_if_sorted(arr,n):
    count=0
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            count+=1
    if count ==0:
        return True
    else:
        return False
#print(check_if_sorted([1,3,6,9,0],5))
        
# time complexity: O(n) => optimal solution


def check_if_array_is_sorted(arr,n):
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            return False
    return True
print(check_if_array_is_sorted([1,3,6,9,9,0],6))