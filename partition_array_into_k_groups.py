from typing import List
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        set_nums=set(nums)
        if len(set_nums)==len(nums) and len(nums)%k==0: 
            return True
        if len(nums)%k!=0:
            return False
        nb_groups=len(nums)/k
        _map={}
        _max_element=1
        for i in nums:
            if i in _map:
                _map[i]+=1
                if _map[i]>_max_element:
                    _max_element=_map[i]
            else:
                _map[i]=1
        if _max_element>nb_groups:
            return False
        # if _max_element==1 and 
        return True
tests=[ 
    ([35,39,65,101,101,54,1,111,8,107,96,90,91,54,115,36,46,76,111,39,29,122,4,113,101,73,125,39,124,33,82,39], 16, False), 
    ([2,2,5,6], 2,True)
    ]
for (list, k,expected_results) in tests: 
    res=Solution().partitionArray(list, k)
    print(res==expected_results, res, expected_results)