# problem: Given two sorted arrays, merge them so that the final array is also sorted

def merge(arr1,arr2): # this is a 2-way mergeSort
    n=len(arr1)
    m=len(arr2)
    i=0
    j=0
    ans=[]
    while (i < n and j < m):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i+=1
        else:
            ans.append(arr2[j])
            j+=1
    
    ans.extend(arr1[i:])
    ans.extend(arr2[j:])
        
    return ans
print(merge([1,2,2,3,4],[5,5,6,7,9,10,11]))

# time complexity: O(nlogn)
# space complexity: O(n)