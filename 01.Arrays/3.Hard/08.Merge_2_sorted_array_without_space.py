# QUESTION:
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, 
# where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

def merge_2sorted_arrays_without_space(nums1,m,nums2,n):
   i=m-1
   j=n-1
   k=(n+m)-1
   while i >= 0 and j >=0:
       if nums1[i] > nums2[j]:
           nums1[i],nums1[k]=nums1[k],nums1[i]
           i-=1
           k-=1
       else:
           nums2[j],nums1[k]=nums1[k],nums2[j]
           j-=1
           k-=1
   while j > 0:
       nums2[j],nums1[k]=nums1[k],nums2[j]
       j-=1
       k-=1
      
       
   while i > 0:
        nums1[i],nums1[k]=nums1[k],nums1[i]
        i-=1
        k-=1
   return nums1
print(merge_2sorted_arrays_without_space([1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
    
        
           