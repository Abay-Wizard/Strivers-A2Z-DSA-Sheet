# Question:
# You are given an integer array bloomDay, an integer m, and an integer k. You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

# The garden consists of n flowers, where the i-th flower will bloom on the bloomDay[i] day and can be used in exactly one bouquet.

# Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets, return -1.

# Example:

# Input:
# bloomDay = [1,10,3,10,2]
# m = 3
# k = 1

# Output:
# 3

# Explanation:
# Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
# We need 3 bouquets each should contain 1 flower.
# After day 1: [x, _, _, _, _]   // we can only make one bouquet.
# After day 2: [x, _, _, _, x]   // we can only make two bouquets.
# After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.

def minDayBouquet(bloomDay,m,k): # brute force approach
    low,high=min(bloomDay),max(bloomDay)+1
    n=len(bloomDay)
    if n < m*k:
        return -1
    for i in range(low,high):
        if Possible(bloomDay,i,m,k):
            return i
    return -1

def Possible(bloomDay,day,m,k):
    counter=0
    Bouq_count=0
    for i in bloomDay:
        if i <=day:
            counter+=1
        else:
            Bouq_count+=(counter//k)
            counter=0
    Bouq_count+=(counter//k)
    if Bouq_count >= m:
        return True
    else:
        return False
    
#print(minDayBouquet([1,10,3,10,2],3,1))

# time complexity: O(n*m)
# space complexity: O(1)


def minDays(bloomDay,m,k):
    n=len(bloomDay)
    low,high=min(bloomDay),max(bloomDay)
    ans=None
    if n < m*k:
        return -1
    while low <=high:
        mid=(low+high)//2
        if Possible(bloomDay,mid,m,k):
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
print(minDays([1,10,3,10,2],3,1))

# time complexity:O(nlogm)
# space complexity: O(1)
