# Write any import statements here

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  # Write your code here
  results=0
  for i in range(N): 
    if C[i]=='A': 
        p_left=max(0, i-Y)
        p_right=max(0, i-X+1)
        has_P_left='P' in C[p_left:p_right]
        has_B_left='B' in C[p_left:p_right]
        b_left=min(i+X, N)
        b_right=min(i+Y+1, N)
        has_B_right='B' in C[b_left: b_right]
        has_P_right='P' in C[b_left: b_right]

        if (has_P_left and has_B_right) or (has_B_left and has_P_right):
            results+=1            
  return results

tests=[
    (8, '.PBAAP.B', 1,3,3), 
    # (5, 'APABA', 1, 2, 1)ß
]
for (N, C, X, Y, expected_results) in tests: 
    res=getArtisticPhotographCount(N, C, X, Y)
    print (res==expected_results, res)