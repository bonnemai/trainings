from typing import List
# Write any import statements here
def cost(i:int, j: int, n:int=10):
    if i==j: 
      return 0
    return min(n-abs(i-j), abs(j-i)) 


def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  # Write your code here
  results=cost(1,C[ 0], N)
  for i in range(M-1): 
    results+=cost(C[i],C[ i+1], N)
  return results


tests=[
    (10, 1, [2], 1),
    (10, 1, [10], 1),
    (10, 1, [9], 2),
    (10, 4, [2,3,4,5], 4),
    (3,3,[1,2,3], 2), 
    (10, 4, [9, 4, 4, 8], 11)
]
for (N,M,C,expected_results) in tests:
    res=getMinCodeEntryTime(N,M,C)
    print(res==expected_results, res)
# print(cost(1, 10, 10))
# print(cost(1, 1, 10))
# print(cost(1, 2, 10))