# QUESTION:
# Given an unsorted array Arr of size N of positive integers. 
# One number 'A' from set {1, 2,....,N} is missing and one number 'B' occurs twice in the array. 
# Find these two numbers.

def find_repeating_missing(nums):
    hashMap={}
    repeating=-1
    n=len(nums)
    missing=-1
    for num in nums:
        hashMap[num]=hashMap.get(num,0)+1
    for i in range(1,n+1):
        if hashMap.get(i)==2:
            repeating=i
        elif i not in hashMap:
            missing=i
    return {repeating,missing}
print(find_repeating_missing([2,2]))