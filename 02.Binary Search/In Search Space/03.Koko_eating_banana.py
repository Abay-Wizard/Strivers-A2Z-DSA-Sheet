# QUESTION:
# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

# EXAMPLES:
# Input: piles = [3,6,7,11], h = 8
# Output: 4

# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
import math
def minEatingSpeed(piles,h): # this is brute force approach
    for i in range(1,max(piles)+1):
        if timeReq(i,piles)<=h:
            return i
def timeReq(i,piles):
    totalTime=0
    for num in piles:
        totalTime+=math.ceil(num/i)
    return totalTime


# time complexity: O(n*m) => where m is max(piles) and n is the length of piles
# space complexity: O(1)



def minEatingSpeed_optimal(piles,h):
    low,high=1,max(piles)
    k=None
    while low <= high:
        mid=(low+high)//2
        if timeReq(mid,piles) <=h:
            k=mid
            high=mid-1
        else:
            low=mid+1
    return k
print(minEatingSpeed_optimal([3,6,7,11],8))

# time complexity: O(nlogn)
# space compelxity:O(1)
            