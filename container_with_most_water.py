from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height)<=1:
            return 0
        result=0

        i_left=0
        i_right=len(height)-1
        result=0
        while i_left<i_right:
            print(i_left)
            volume=(i_right-i_left)*min(height[i_left], height[i_right])
            if volume>result:
                result=volume
            if height[i_left]<height[i_right]: 
                i_left+=1
            else:
                i_right-=1

        return result
s=Solution()
tests=[
    ([1,8,6,2,5,4,8,3,7], 49),
    # ([1,8,6,2,5,4,8,3,7], 9)
]
for (height, expected_results) in tests:
    res=s.maxArea(height)
    print(res==expected_results, height, res, expected_results)