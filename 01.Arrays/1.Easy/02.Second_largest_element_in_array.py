# Given an array Arr of size N, print second largest distinct element from an array.
# for example input n=6, arr=[24,63,92,74,20,82] and output will be => 82

# approach 1: Sorting the array and traversing starting from the second last element and check if it is smaller than the largest element.
# And this approach is the most generic solution and called brute force approach.
# approach 2: Finding the largest element first, and repeat the same logic skipping the largest element(if any repeated max_values) to find the 2nd largest.

# approach 3: if the current element is greater than 'large' then update 'second_large' and 'large' and
# if this is not true and if current element is greater than 'second_large' and not equal to 'large' update the 'second_large'
# when done with traversing, we get the second largest element.

def find_2nd_largest_bysorting(arr,n):
    arr.sort()
    #print(arr)
    max=arr[n-1]
    sec_max=-1
    for i in range(n-2,-1,-1):
        if arr[i] < max:
            sec_max=arr[i]
            break
    return sec_max
print(find_2nd_largest_bysorting([1,2,2,1,2,4,7],7))
            
# time complexity is (O(n)log(n) + O(n)) => very expensive



def find_2nd_largest(arr,n): # this works for all negative and positive numbers.
    Max=arr[0]
    for i in range(1,n):
        if arr[i] > Max:
            Max=arr[i]
    Sec_Max=None
    for i in arr:
        if i==Max:
            continue
        elif Sec_Max==None or i > Sec_Max:
            Sec_Max=i
    return Sec_Max
# time complexity(O(2n)) =>better solution



def get_2nd_largest(nums,n): # the inputs should always be free of negative nums for this code to work as intended.
    second_large=-1
    large=nums[0]
    for i in range(1,n):
        if nums[i] >large:
            second_large=large
            large=nums[i]
        elif nums[i] > second_large and nums[i] !=large:
            second_large=nums[i]
    return second_large
#print(get_2nd_largest([1,2,2,1,2,4,7],7))
# time complexity(O(n)) => optimal solution


    