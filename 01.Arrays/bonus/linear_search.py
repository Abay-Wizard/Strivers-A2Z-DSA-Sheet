# Given array and specific value from the array, return the first occurence index of that value
def linear_search(arr,val):
    n=len(arr)
    for i in range(n):
        if arr[i]==val:
            return i
print(linear_search([1,2,6,3,9],3))