
def count_peaks(arr): 
    count=0
    threshold=5
    for i in range(1,len(arr)-1):
        if arr[i]>arr[i-1]+threshold and arr[i]>arr[i+1]+threshold:
            count+=1
        if arr[i]>arr[i-1]-threshold and arr[i]>arr[i+1]-threshold:
            count+=1

    return count

tests=[
    ([0,10,0,10,0,10,0, 10,0,10],8),
]
for arr, expected in tests:
    assert count_peaks(arr)==expected
    print(f"Test passed for {arr} with expected {expected}")
print("All tests passed")