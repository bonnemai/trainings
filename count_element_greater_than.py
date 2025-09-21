def countResponseTimeRegressions(responseTimes):
    # Write your code here
    _sum=0
    results=0
    for i in range(0,len(responseTimes)): 
        if i>0:
            if responseTimes[i]>(_sum/i): 
                results+=1
        _sum+=responseTimes[i]
    return results

tests=[
    ([1,2,3,4,5], 4),
    ([5,4,3,2,1], 0),
    ([100, 200, 150,300], 2),
]
for input, expected in tests: 
    result=countResponseTimeRegressions(input)
    print(f'input: {input}, expected: {expected}, result: {result}, pass: {expected==result}')