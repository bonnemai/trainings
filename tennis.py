


def get_value(i): 
    _map={0:0, 1:15, 2:30, 3:40}
    return _map[i]

def winner(_map): 
    if _map['A']>_map['B']: 
        return 'A'
    elif _map['A']<_map['B']: 
       return 'B'
    

def tennis(arr): 
    """
    Rules: 
        A 15 - B 30 
        15a/ 30a/ 40a
        A Wins
        A Advantage: >40 and player A has 1 point more than b
    """
    _map={'A': 0, 'B': 0}
    for a in arr: 
        _map[a]+=1
    if _map['A']>3 or _map['B']>3:
        if _map['A']>_map['B']+1:
            return 'A Wins'
        elif _map['B']>_map['A']+1:
            return 'B Wins'
        elif _map['A']>_map['B']:
            return 'A Advantage'
        elif _map['B']>_map['A']+1:
            return 'B Advantage'
    elif _map['A']==_map['B']: 
        return f"{get_value(_map['A'])}a"
    else:
        return f"A {get_value(_map['A'])} - B {get_value(_map['B'])}"

tests=[
    (['A', 'B'], '15a'),
    (['A', 'B', 'A', 'B'], '30a'),
    (['A', 'A', 'A', 'A'], 'A Wins')
]
for (arr, expected_result) in tests:
    res=tennis(arr)
    print(res==expected_result, res)