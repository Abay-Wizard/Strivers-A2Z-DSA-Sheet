# find the intersection of two sorted arrays
def find_intersection_of_sorted_arrays(arr1,arr2):
    intersection=[]
    n1=len(arr1)
    n2=len(arr2)
    i=0
    j=0
    while (i < n1 and j < n2):
        if arr1[i]==arr2[j]:
            if not arr1[i] in intersection:
                intersection.append(arr1[i])
                i+=1
                j+=1
        else:
            i+=1
    return intersection
print(find_intersection_of_sorted_arrays([1,2,5,6,9],[1,6,9,18,19,30]))