from typing import List
from itertools import combinations
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results=[]
        current=['()']
        i=0
        # for i in range(n): 
        #     current=initial
            # current=initial
            # for i in initial: 
        while i<n:
            for s in current: 
                results.append(f'({s})')
                results.append(f'{s}()')
            i+=1
            # initial=current
        return current
        # combs=list(combinations([0,1,2,3], n))
        # # print(combs[0])
        # for comb in combs: 
        #     print(comb)
        #     # for c in comb:
        #     #     print (c)
        # return '()'
        # results1 = []
        # results2 = []
        # results3 = []
        # for i in range(1,n+1): 
        #     results1.append('()'*i)
        # for res in results1: 
        #     results2.append(f'({res})')
        # print(results2)
        # for res in results2: 
        #     while len(res)!=2*n: 
        #         res = f'({res})'
        #     results3.append(res)
        # return results3
tests=[
    (3)
]
for (n) in tests:
    res=Solution().generateParenthesis(n)
    print (res)