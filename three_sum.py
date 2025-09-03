from itertools import combinations
from typing import List

# from itertools import combinations

def can_add(results: [], res):
    for r in results: 
        if r[0]==res[0] and r[1]==res[1] and r[2]==res[2]: 
            return False
    return True


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<=2: 
            return []
        _map={}
        results=[]
        for i in range(len(nums)):
            for j in range(i, len(nums)): 
                if nums[i] not in _map or nums[j] not in _map[nums[i]]: 
                    remaining=-1*(nums[i]+nums[j])
                    if remaining in nums[j+1:]:
                        results.append([nums[i], nums[j], remaining])
                        if nums[i] not in _map: 
                            _map[nums[i]]=[nums[j]]
                        else: 
                            _map[nums[i]].append(nums[j])
        return results

# def can_add(results: [], res):
#     for r in results: 
#         if r[0]==res[0] and r[1]==res[1] and r[2]==res[2]: 
#             return False
#     return True


# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         combs=combinations(nums, 3)
#         results=[]
#         for c in combs:
#             # print (c)
#             if c[0]+c[1]+c[2]==0:
#                 res=[c[0], c[1], c[2]]
#                 res.sort()
#                 if can_add(results, res): 
#                     results.append(res)
#         return results
s=Solution()
# s.threeSum([1,2,3, 4, 5])
tests=[
    ([-1,0,1,2,-1,-4], [[-1,0,1], [-1,-1,2]]),
    ([0,0,0], [[0,0,0]])
    ]
for (nums, expected_results) in tests: 
    results = s.threeSum(nums)
    print(results == expected_results, nums, results, expected_results)