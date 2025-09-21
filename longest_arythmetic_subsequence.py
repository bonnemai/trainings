def findLongestArithmeticProgression(arr, k):
    # Write your code here
    arr=sorted(set(arr))
    # Maybe loop on k later
    if len(arr)==0:
        return 0
    response=0
    for i in range(k): 
        if len(arr)>i:
            progression=[arr[i]]
            next_elements=[a for a in arr if a>=progression[-1]+k]
            has_next_element=len(next_elements)>0
            while has_next_element: 
                progression.append(next_elements[0])
                next_elements=[a for a in arr if a>=progression[-1]+k]        
                has_next_element=len(next_elements)>0
            response=max(response, len(progression))
    return response

tests=[
    # ([42], 7, 1),
    # ([1,7,10,13,14,19], 3, 4),
    ([2,4,6,8], 2, 4),
    ([1,3,5,7], 1, 1),
]
for input, k, expected in tests:
    result=findLongestArithmeticProgression(input, k)
    print(f'input: {input}, k: {k}, expected: {expected}, result: {result}, pass: {expected==result}')