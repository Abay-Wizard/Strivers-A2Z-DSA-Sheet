# Question:-
# Given two sorted arrays arr1 and arr2 of size N and M respectively and an element K.
# Find the element that would be at the kth position of the final sorted array.

# Example:- 

# Input:
# arr1[] = {2, 3, 6, 7, 9}
# arr2[] = {1, 4, 8, 10}
# k = 5
# Output:
# 6
# Explanation:
# The final sorted array would be -
# 1, 2, 3, 4, 6, 7, 8, 9, 10
# The 5th element of this array is 6.

def kth_element_sorted_arrays(nums1,nums2,k):
    if len(nums1) > len(nums2):
        nums1,nums2=nums2,nums1
    n1,n2=len(nums1),len(nums2)
    left=k
    low,high=max(0,k-n2),min(k,n1)
    while low <=high:
        mid1=(low+high)//2
        mid2=left-mid1
        L1,L2=float('-inf'),float('-inf')
        r1,r2=float('inf'),float('inf')
        if mid1 < n1:
            r1=nums1[mid1]
        if mid2 < n2:
            r2=nums2[mid2]
        if (mid1-1) >=0:
            L1=nums1[mid1-1]
        if (mid2-1) >=0:
            L2=nums2[mid2-1]
        if (L1 <=r2 and L2 <= r1):
            return max(L1,L2)
        elif L1 > r2:
            high=mid1-1
        else:
            low=mid1+1
print(kth_element_sorted_arrays([2, 3, 6, 7, 9],[1, 4, 8, 10],7))
    