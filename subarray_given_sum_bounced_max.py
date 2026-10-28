def countSubarraysWithSumAndMaxAtMost(nums, k, M):
    if len(nums)<1:
        return 0
    left=0
    right=1
    results=0
    while left!=len(nums)-2:
        if max(nums[left:right])>M or right==len(nums)-1:
            left+=1
        elif sum(nums[left:right])==k:
            results+=1
        right+=1
    return results

tests=[
    ([2,-1,2,1,-2,3], 3,2,2)
]
for nums, k,M,expected in tests:
    res=countSubarraysWithSumAndMaxAtMost(nums, k, M)
    print(res==expected, res, expected, nums)