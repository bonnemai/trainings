def mediane(arr): 
    arr.sort()
    if len(arr)%2==0: 
        median = (arr[len(arr)//2 - 1]+arr[len(arr)//2 ])/2. 
    else:   
        median = arr[len(arr)//2] 
    return median

tests=[
    ([1, 3, 3, 6, 7, 8, 9], 6),
    # ([1, 2, 3, 4], 2.5),
    ([1,2,5,4], 2), 
    ([2,5,4], 4)
]
for arr, expected_results in tests:
    assert mediane(arr) == expected_results, f"expected {expected_results}, got {mediane(arr)}: {arr}"