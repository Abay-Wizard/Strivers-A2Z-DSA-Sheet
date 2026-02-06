# Question:
# A conveyor belt has packages that must be shipped from one port to another within days days.

# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

# Example:

# Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
# Output: 15
# Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
# 1st day: 1, 2, 3, 4, 5
# 2nd day: 6, 7
# 3rd day: 8
# 4th day: 9
# 5th day: 10

def minCapacity(weights,days):
    low=max(weights)
    tot_sum=sum(weights)
    for i in range(low,tot_sum):
        if daysReq(weights,i) <=days:
            return i

def daysReq(weights,capacity):
    days,load=1,0
    for i in weights:
        if load+i > capacity:
            days+=1
            load=i
        else:
            load+=i
    return days


# time complextiy: O(n*m)
# space complexity: O(1)

def minCapacity_optimal(weights,day):
    low,high=max(weights),sum(weights)
    while low <=high:
        mid=(low+high)//2
        if daysReq(weights,mid) <=day:
            high=mid-1
        else:
            low=mid+1
    return low
print(minCapacity_optimal([1,2,3,4,5,6,7,8,9,10],5))
        
    