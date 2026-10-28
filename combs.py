from itertools import combinations
def countValidSubarrays(n, a, k):
    results=0
    for i in range(1, n+1):
        combs=combinations(a, i)
        for comb in combs:
            print(list(comb))
            if max(comb)-min(comb)<=k:
                results+=1
    return results 

tests=[
    ([1], 5, 1),
    # ([1,2,3], 2, 6)
]
for a, k, expected_results in tests:
    res=countValidSubarrays(len(a), a, expected_results)
    assert res==expected_results, f'res: {res}, exp: {expected_results}'
