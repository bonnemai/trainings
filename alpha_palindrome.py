def isAlphabeticPalindrome(code):
    if len(code)==0:
        return True
    left=0
    right=len(code)-1
    while left<=right:
        if not code[left].isalpha():
            left+=1
        if not code[right].isalpha():
            right-=1
        if code[left].isalpha() and code[right].isalpha(): 
            if code[left].lower()!=code[right].lower():
                return False
        left+=1
        right-=1
    return True


tests=[('A1b2B!a', True), 
       ('', True), 
       ('!!!!!!!!', True)
       ]
for code, expected in tests:
    results = isAlphabeticPalindrome(code)
    print(results==expected, 'Results', results)