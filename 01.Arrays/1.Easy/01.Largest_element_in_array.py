# Given the length of array(n). Find the largest element of the array.
# for example, input n=5 and arr=[30,94,28,47,82] => output will be 94 
def find_largest(arr,n):
    Max=arr[0]
    for i in range(1,n):
        if arr[i] > Max:
            Max=arr[i]
    
    return Max
print(find_largest([30,94,28,47,82],5))