
def diagonalDifference(arr):
    # Write your code here
    diag1=0
    diag2=0
    for i in range(len(arr)): 
        # for j in range(len(arr[0])): 
        diag1+=arr[i][i] 
        diag2+=arr[len(arr)-i-1][i]
    return abs(diag2-diag1)
arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
print(diagonalDifference(arr))