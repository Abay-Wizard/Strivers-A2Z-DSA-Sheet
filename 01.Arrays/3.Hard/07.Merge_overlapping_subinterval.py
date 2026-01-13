# QUESTION:
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals and return an array of non-overlapping intervals that cover all the intervals in the input.

# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].


def merge_intervals_brute(intervals):
    intervals.sort()
    final_intervals=[]
    n=len(intervals)
    for i in range(n):
        start=intervals[i][0]
        end=intervals[i][1]
        if len(final_intervals) > 0 and end <= final_intervals[-1][1]:
            continue
        for j in range(i+1,n):
            if intervals[j][0] <=end:
                end=max(end,intervals[j][1])
            else:
                break
        final_intervals.append([start,end])
            
            
    return final_intervals
print(merge_intervals_brute([[1,3],[2,6],[8,10],[15,18]]))



def merge_intervals(intervals):
    intervals.sort()
    mer_int=[intervals[0]]
    start,end=0,1
    n=len(intervals)
    for i  in range(1,n):
        if intervals[i][start] <= mer_int[-1][end]:
            mer_int[-1]=[intervals[i][start],max(intervals[i][end],mer_int[-1][end])]
        else:
            mer_int.append(intervals[i])
    return mer_int
