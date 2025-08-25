from itertools import combinations
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if i!=j and nums[i]+nums[j]==target:
                        return [i,j]
        # comb=combinations(range(len(nums)), 2)
        # for it in comb:
        #     sum=0
        #     results=[]
        #     for i in range(len(it)):
        #         sum+=nums[it[i]]
        #         results.append(it[i])
        #     if sum==target:
        #         return results


if __name__ == "__main__":
    sol=Solution()
    print(sol.twoSum([2,7,11,15],9))
    print(sol.twoSum([3,2,4],6))
    print(sol.twoSum([3,3],6))
    print(sol.twoSum([1,2,3,4,5],3))
    print(sol.twoSum([1,2,3,4,5,6,7,8,9,10],10))
    
