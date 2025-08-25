
ONE_STATE=1
TWO_STATE=2
def eliminate(s: str):
    results=[]
    state=ONE_STATE
    for i in range(len(s)):
        _char=s[i]
        if _char=='b':
            continue
        if _char=='a':
            state=TWO_STATE
            continue
        if _char=='c' and state==TWO_STATE:
            state=ONE_STATE
            continue
        if state==TWO_STATE:
            state=ONE_STATE
        results.append(_char)

    return ''.join(results)


# Eliminate b and ac:
if __name__ == "__main__":
    tests = [
        ("abc", "ac"),
        ("acbac", ""),
        ("aaac", "aa"),
        ("ababac", "aa"),
        ("bbbbd", "d"),
    ]
    for (s, expected_results) in tests:
        results = eliminate(s)
        print('Res: ', s, results, expected_results)