from itertools import combinations
#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    combs=combinations(s, 2)
    potentials=set()
    for comb in combs: 
        if (comb[0]+comb[1])%k!=0: 
            potentials.add(comb[0])
            potentials.add(comb[1])
            # print('Adding ', comb, comb[0]+comb[1]%k)
    print (potentials)
    return len(potentials)

tests=[
    (11, [278, 576, 496, 727, 410, 124, 338, 149 ,209 ,702, 282, 718, 771, 575, 436], 11),
    # (3, [1, 7, 2, 4], 3)
]
for (k, s, expected_results ) in tests:
    res=nonDivisibleSubset(k, s)
    print(res==expected_results, res)