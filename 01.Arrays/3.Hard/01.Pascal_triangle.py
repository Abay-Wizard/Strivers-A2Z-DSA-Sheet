# Problem 1:  Given two numbers n, and r find their combination

def find_combination(n,r):
    result=1
    for i in range(r):
        result=result*(n-i)
        result=result//(i+1)
    return result


# Problem 2: Given the row(R) and column(C) find the element at that particular place from pascal's triangle

def find_element_from_pascal_triangle(R,C):
    return find_combination(R,C) # assuming the question follows 0-based indexing, otherwise we always have to subtract 1 from
#column and row to get the correct mathematical expression


# time complexity: O(C)
# space complexiy: O(1)

# Problem 3: Given the row(N) of a pascal's triangle, print all the elements in that particular row

def print_row_elements(n): # this is brute force approach
    for c in range(1,n+1):
        print(find_element_from_pascal_triangle(n,c))
        
# time complexity: O(n^2)
# space complexity: O(1)


def print_row_elements_optimal(n):
    ans=1
    row_elems=[ans]
    for c in range(n):
        ans=ans*(n-c)
        ans=ans//(c+1)
        row_elems.append(ans)
    return row_elems


# time complexity: O(n)
# space complexity: O(n)

# Problem 4: Given rowIndex of pascal's triangle, print the entire triangle up till that row, which is basically a list of
# of lists of each row elements

def print_entire_triangle(rowIndex):
    large_elems=[]
    for i in range(rowIndex):
        large_elems.append(print_row_elements_optimal(i))
    return large_elems
print(print_entire_triangle(6))

# time complexity: O(n^2)
# space complexity: O(n)