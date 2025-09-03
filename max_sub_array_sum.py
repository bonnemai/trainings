class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        results=arr[0]
        tmp=arr[0]
        for i in range(1, len(arr)): 
            tmp=max(tmp+arr[i], arr[i])
            results=max(tmp, results)
        # i_left=0
        # i_right=len(arr)-1
        # results=sum(arr)
        # if i_right>1: 
        #     while i_left<i_right: 
        #         if arr[i_left]<=arr[i_right]: 
        #             results-=arr[i_left]
        #             i_left+=1
        #         else:
        #             results-=arr[i_left]
        #             i_right-=1

        #         # if i_left==i_right:
        #         #     return results
        #         _sum=sum(arr[i_left:i_right])
        #         if _sum>results:
        #             results=_sum

        return results
tests=[
        ([5 ,-3, 7, 6, 5], 20),
        ([-3 ,-2 ,-6 ,-1 ,-7 ,-4], -1), 
        ([1], 1),
]

for (arr, expected_results) in tests:
    res=Solution().maxSubarraySum(arr)
    print (res==expected_results, res)