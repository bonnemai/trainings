from typing import List



def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
  # Write your code here
    frogs=[False]*N
    results=0
    for frog in P: 
        frogs[frog-1]=True
    for i in range(N-1): 
        if frogs[i]: 
            j=i
            while j<N and frogs[j]: 
                j+=1
            frogs[i]=False
            if j<N:
                frogs[j]=True
            results+=1
    return results
#   P.sort()
#   #//_map={}
#   results=0
#   for start in P: 
#     end=start+1
#     while end in P and end!=N: 
#       end+=1
#     del P[0]
#     results+=1
#     if end<=N: 
#       P.append(end)
#       P.sort()
            
#   return results

tests=[
    (6, 3, [1, 2, 3], 4),
    (3,1,[1], 2), 
    (6, 3, [5, 2, 4], 4)
]
for(N, F, P, ex_res) in tests:
    res=getSecondsRequired(N,F,P)
    print (res==ex_res, res)