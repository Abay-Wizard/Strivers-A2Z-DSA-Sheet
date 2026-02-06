# Questions:-
# We have an horizontal number line. On that number line, we have gas stations at positions stations[0], stations[1], ..., stations[N-1], where N = size of the stations array. Now, we add K more gas stations so that D, the maximum distance between adjacent gas stations, is minimized. We have to find the smallest possible value of D. Find the answer exactly to 2 decimal places.

# Example 1:

# Input:
# N = 10
# stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# K = 9
# Output: 0.50
# Explanation: Each of the 9 stations can be added mid way between all the existing adjacent stations.
# Example 2:

# Input:
# N = 10
# stations = [3,6,12,19,33,44,67,72,89,95]
# K = 2
# Output: 14.00
# Explanation: Construction of gas stations at 86 locations

def minMaxGasStations(stations,k):
    n=len(stations)
    howMany=[0]*(n-1)
    for i in range(k):
        maxi_length,maxi_index=-1,-1
        for i in range(n-1):
            section_length=(stations[i+1]-stations[i])/(howMany[i]+1)
            if maxi_length < section_length:
                maxi_length=section_length
                maxi_index=i
        howMany[maxi_index]+=1
    
    maxAns=-1
    for i in range(n-1):
        section_len=(stations[i+1]-stations[i])/(howMany[i]+1)
        maxAns=max(maxAns,section_len)
    return maxAns

# time complexity: O(k*n)
# space complexity: O(n)

def minMaxGasStations_optimal(stations,k):
    low,high=0,(stations[-1]-stations[0])
    while (high-low > 1e-6):
        mid=(low+high)/2.0
        if stationsReq(stations,mid) > k:
            low=mid
        else:
            high=mid
    return round(high,2)

def stationsReq(stations,dist):
    n=len(stations)
    count_stations=0
    for i in range(n-1):
        segment_gap=stations[i+1]-stations[i]
        numsInBetween=int(segment_gap/dist)
        if segment_gap % dist ==0:
            numsInBetween-=1
        count_stations+=numsInBetween
    return count_stations

print(minMaxGasStations_optimal([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],10))