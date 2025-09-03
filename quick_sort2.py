# def partition(arr, low, high): 
#     for i in range(low, high):
#         if arr[i]>arr[high]:
#             arr[i], arr[high]=arr[high], arr[i]
#     return i+1
# def quick_sort(arr, low, high):
#     if low<high: 
#         pi=partition(arr, low, high)
#         quick_sort(arr, low, pi-1)
#         quick_sort(arr, pi+1, high)

# arr=[1,2,3,4,5]
# quick_sort(arr, 0,len(arr)-1 )
# print (arr) 