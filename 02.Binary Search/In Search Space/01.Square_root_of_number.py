# Given an integer x, find the square root of x. If x is not a perfect square, then return floor(√x).

def find_sqrt(num):
    low,high=0,num
    ans=0
    while low <= high:
        mid=(low+high)//2
        if mid*mid <=num:
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return ans
print(find_sqrt(9))