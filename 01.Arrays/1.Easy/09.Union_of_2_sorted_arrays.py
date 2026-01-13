# problem: finding the union of two sorted arrays
def find_union_of_sorted_arrays(arr1,arr2): # brute force approach
   union=[]
   for i in arr1:
       if not i in union:
           union.append(i)
   for j in arr2:
        if not j in union:
            union.append(j)   
   union.sort()
   return union
print(find_union_of_sorted_arrays([2,3,22,92],[1,2,3,4,5]))

# Optimal solution
def find_union_of_sorted_arrays_opt(arr1,arr2):
    union=[]
    n1=len(arr1)
    n2=len(arr2)
    i=0
    j=0
    while (i < n1 and j < n2):
        if arr1[i] <=arr2[j]:
            if not arr1[i] in union:
                union.append(arr1[i])
            i+=1
        else:
            if not arr2[j] in union:
                union.append(arr2[j])
            j+=1
    
    while i < n1:
        if not arr1[i] in union:
            union.append(arr1[i])
        i+=1
    
    
    while j < n2:
        if not arr2[j] in union:
            union.append(arr2[j])
        j+=1
    
    return union
#print(find_union_of_sorted_arrays_opt([1,2,5,6,8],[2,3,22,92]))
        
    

def find_intersection_of_arrays(arr1,arr2):
    intersection=[]
    for i in arr1:
        if (i in arr2 and i not in intersection):
            intersection.append(i)
    return intersection
#print(find_intersection_of_arrays([1,2,5,6,8],[2,0,0,22,92]))