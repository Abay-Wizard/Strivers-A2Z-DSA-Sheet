# problem: find majority element in a given array, majority element is the one which occurs more than (n/2) times where n is the length of the Arrays
# approach: initializing two variables, one for candidate and the other count and start iterating from the second
# element, if the elements next to the candidate are similar to it, we increase the count by one, othewise, we decrease 
# count by one, if count becomes zero, we reinitialize the candidate as the value at that particular index and count as 1
# finally candidate becomes the answer we are trying to solve for

def majority_element(nums): # Moore's voting theorem
    n=len(nums)
    candidate=nums[0]
    count=1
    for i in range(1,n):
        if count==0:
            candidate=nums[i]
            count+=1
        elif nums[i]==candidate:
            count+=1
        else:
            count-=1
            
    return candidate
            
print(majority_element([2,2,1,1,1,2,2]))
            
             