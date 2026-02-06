# Question:
# In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

# Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

# Given the integer array position and the integer m. Return the required force.

# Example:

# Input: position = [1,2,3,4,7], m = 3
# Output: 3
# Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.

def maxMinForce(arr,m): # brute force approach
    arr.sort()
    high=max(arr)-min(arr)
    for i in range(1,high):
        if Possible(arr,i,m):
            continue
        else:
            return i-1

def Possible(arr,dist,balls):
    n=len(arr)
    ball_count,last=1,arr[0]
    for i in range(1,n):
        if arr[i]-last >=dist:
            ball_count+=1
            last=arr[i]
    if ball_count >=balls:
        return True
    else:
        return False

# time complexity: O(high * n)
# space complexity: O(1)

def maxMinForce_optimal(arr,m):
    arr.sort()
    low,high=0,max(arr)-min(arr)
    ans=None
    while low <= high:
        mid=(low+high)//2
        if Possible(arr,mid,m):
            low=mid+1
            ans=mid
        else:
            high=mid-1
    return ans

print(maxMinForce_optimal([1,2,3,4,7],3))

# time complexity: O(log(high)*n)
# space complexity: O(1)