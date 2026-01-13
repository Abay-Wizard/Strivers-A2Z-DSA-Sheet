'''
QUESTION:-
Given an array "ARR' containing 'N' elements, rotate this array Left by once means to shift all elements by one place to the left and move the first element to the last position in the array.

Example:
Input: 'N' 5, 'ARR' = [1, 2, 3, 4, 5]
Output: [2, 3, 4, 5, 1]

Explanation:
We moved the 2nd element to the 1st position and 3rd element to the 2nd position and 4th element to the 3rd position and 5th element to the 4th position and move oth element to the 5th position.

'''
def rotate_array_to_left_by1place(arr,n):
    k=0
    for j in range(1,n):
        arr[k],arr[j]=arr[j],arr[k]
        k+=1
    return arr
#print(rotate_array_to_left_by1place([1, 2, 3, 4, 5],5))

# another approach, reversing the 1st k elements, and reversing the last n-k elements, and finally reversing the entire array

def rotate_to_left_byk_place(arr,k):
    arr[:k]=reversed(arr[:k])
    arr[k:]=reversed(arr[k:])
    arr[:]=reversed(arr[:])
    return arr
print(rotate_to_left_byk_place([1, 2, 3, 4, 5],1))