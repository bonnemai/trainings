# Return Sorted Array
# Given an array sorted by its absolute values, return sorted array by it actually values - Solve in O(N)
# // example 
# input: 0,-1, 2, -4,5, 6, -10, -13, -22
# output: -22, -13, -10, -4, -1,0, 2, 5, 6

def sorted_array(arr):
    n = len(arr)
    negative_result = []
    positive_result = []
    for i in range(n):
        if arr[i] < 0:
            negative_result.append(arr[i])
    for i in range(n):
        if arr[i] >= 0:
            positive_result.append(arr[i])
    negative_result.reverse()
    return negative_result + positive_result
    # left, right = 0, n - 1

    # left, right = 0, n - 1
    # result = []
    # while left <= right:
    #     if arr[right] < 0 and arr[right] <=arr[left]:
    #         result.append(arr[right])
    #         right -= 1
    #     else:
    #         result.append(arr[left])
    #         left += 1
    return result
    # return result[::-1]

# Example usage
input_array = [0, -1, 2, -4, 5, 6, -10, -13, -22]
output_array = sorted_array(input_array)
print(output_array)  # Output: [-22, -13, -10, -4, -1, 0, 2, 5, 6]
# // Time Complexity: O(N)
# // Space Complexity: O(N)