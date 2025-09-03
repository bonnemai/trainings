# from b_ac import expected_results


def findEquilibrium(arr):
    
    n=len(arr)
    if n<=2:
        return -1
    left_sum=arr[0]
    right_sum=sum(arr[2:])
    for i in range(1, len(arr)):
        left_sum+=arr[i]
        if i+1>=n:
            return -1
        right_sum-=arr[i+1]
        if left_sum == right_sum:
            return i+1
    return -1

tests=[
    ([1 ,2, 0, 3], 2), 
    ([1 ,1, 1, 1], -1)]
for (arr, expected_results) in tests: 
    print(findEquilibrium(arr), expected_results)