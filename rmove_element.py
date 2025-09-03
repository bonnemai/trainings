from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        results=0
        n=len(nums)
        for i in range(n): 
            if nums[i]==val:
                nums.pop(i)
                nums.append(val+1)
                results+=1
        # while i<len(nums): 
        #     if nums[i]==val:
        #         nums.pop(i)
        #         results+=1
        #     i+=1
        return results

tests=[
    ([0,1,2,2,3,0,4,2], 2, 2)
]
for nums, val, expected_results in tests:
    res=Solution().removeElement(nums, val)
    print(res==expected_results, res)
    # int[] nums = [...]; // Input array
    # int val = ...; // Value to remove
    # int[] expectedNums = [...]; // The expected answer with correct length.
    #                             // It is sorted with no values equaling val.

    # int k = removeElement(nums, val); // Calls your implementation

    # assert k == expectedNums.length;
    nums.sort() # // Sort the first k elements of nums
    for  i in range( nums) :
        print (nums[i])
        # assert nums[i] == expectedNums[i];
    