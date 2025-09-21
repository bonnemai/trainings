
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot=arr[0]
        left=[x for x in arr[1:] if x<pivot]
        right=[x for x in arr[1:] if x>=pivot]
        return quick_sort(left)+ [pivot]+quick_sort(right)

tests=[
[6, 1,2,3,4,5], 
[3,2,1]
]
for arr in tests: 
    results=quick_sort(arr )
    print (results) 