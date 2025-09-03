def func(param): 
    return param

tests=[
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
]

for param, expected_result in tests:
    res=func(param)
    print(res==expected_result, res, expected_result)