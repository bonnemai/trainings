# Given an array arr[] containing only non-negative integers, your task is to find a continuous subarray (a contiguous sequence of elements) whose sum equals a specified value target. You need to return the 1-based indices of the leftmost and rightmost elements of this subarray. You need to find the first subarray whose sum is equal to the target.

# Note: If no such array is possible then, return [-1].

# Examples:

# Input: arr[] = [1, 2, 3, 7, 5], target = 12
# Output: [2, 4]
# Explanation: The sum of elements from 2nd to 4th position is 12.
# Input: arr[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target = 15
# Output: [1, 5]
# Explanation: The sum of elements from 1st to 5th position is 15.
# Input: arr[] = [5, 3, 4], target = 2
# Output: [-1]
# Explanation: There is no subarray with sum 2.
# Constraints:
# 1 <= arr.size()<= 106
# 0 <= arr[i] <= 103
# 0 <= target <= 109
# def sum_arr(arr):
#     results=0
#     for a in arr: 

# def get_idx(arr, target): 
#     sliding_window=[]
#     i_start=0
#     i_end=0
#     # for a in arr: 
#     if len(arr)==0:
#         return [-1]
#     sliding_window.append(arr[0])
#     _sum=sum(sliding_window)
#     if _sum==target:
#         return [i_start, i_end]
#     elif _sum>target:
#         i_start+=1
#         sliding_window.pop()
#     elif _sum<target:
#         i_end+=1
#         sliding_window.append(arr[i_end])
#     return [-1]




def subarraySum(arr, target): 
    i_start=1
    i_end=1
    if len(arr)==0:
        return [-1]
    sliding_window=[arr[0]]
    _sum=sum(sliding_window)
    while _sum!=target:
        if _sum>target:
            if len(sliding_window)==1 and sliding_window[0]==target:
                return [i_start, i_start]
            if len(sliding_window)>0:
                i_start+=1
                _sum-=sliding_window.pop(0)
            if _sum==target:
                return [i_start, i_end]
        if _sum<target:
            i_end+=1
            if i_end>len(arr):
                return [-1]
            sliding_window.append(arr[i_end-1])
            _sum+=arr[i_end-1]
    return [i_start, i_end]

    
tests=[
    ([37, 25 ,21 ,47, 22, 49, 50, 19, 35, 32, 35], 54, [8,9]),
    # ([7 ,31 ,14 ,19 ,1 ,42 ,13, 6 ,11 ,10, 25, 38, 49, 34, 46, 42, 3 ,1], 42, [6,6]),
    # ([22 ,3, 4, 4, 15, 22, 2, 24, 29], 68, [-1]),
    # ([12,18,5, 11, 30, 5], 69,[2,6]),
    # ([1,2,3,7,5], 12, [2,4]), 
    # ([1,2,3,7,5], 5, [2,3]), 
    # ([1,2,3,7,5], 3, [1,2]), 
    # ([5, 3, 4],  2, [-1]),
    # ([1,1,1],  1000, [-1]),
    # ([12],  12, [1,1])
    ]
for (arr, target, expected_results) in tests:
    print('res', subarraySum(arr, target), expected_results)