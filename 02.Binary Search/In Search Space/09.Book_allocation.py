# Question:
# You have N books, each with Ai number of pages. M students need to be allocated contiguous books, with each student getting at least one book. Out of all the permutations, the goal is to find the permutation where the student with the most pages allocated to him gets the minimum number of pages, out of all possible permutations.

# Note: Return -1 if a valid assignment is not possible, and allotment should be in contiguous order.

# Example:

# Input:
# N = 4
# A[] = {12,34,67,90}
# M = 2
# Output: 113
# Explanation:
# Allocation can be done in following ways:
# {12} and {34, 67, 90} Maximum Pages = 191
# {12, 34} and {67, 90} Maximum Pages = 157
# {12, 34, 67} and {90} Maximum Pages = 113.
# Therefore, the minimum of these cases is 113, which is selected as the output

def minMaxPages(books,m): # brute force approach
    if m > len(books):
        return -1
    low,high=max(books),sum(books)
    for i in range(low,high+1):
         if calculateStudent(books,i)==m:
             return i
def calculateStudent(books,pages):
    count_student,count_pages=1,0
    for book in books:
        if count_pages+book <= pages:
            count_pages+=book
        else:
            count_student+=1
            count_pages=book
    return count_student

# time complexity: O((high-low)*n)
# space complexity: O(1)


def minMaxPages_optimal(books,m):
    low,high=max(books),sum(books)
    while low <=high:
        mid=(low+high)//2
        if calculateStudent(books,mid) > m:
            low=mid+1
        else:
            high=mid-1
    return low

print(minMaxPages_optimal([12,34,67,90],2))

# time complexity: O(log(high-low)*n)
# space complexity: O(1)