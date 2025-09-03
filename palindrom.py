def is_palindrom(s:str)->bool:
    
    for i in range(len(s)//2): 
        if s[i]!=s[len(s)-i-1]:
            return False
    return True

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if is_palindrom(s):
            return s
        for i in range(0, len(s)): 
            length = len(s)-i
            for j in range(len(s)-length+1): 
                substr=s[j:j+length]
                if is_palindrom(substr): 
                    return substr

        return ''
# print(is_palindrom('abba'))
# print(is_palindrom('aba'))
# print(is_palindrom('abbc'))
print(is_palindrom('a'))
tests=[('abb', 'bb'), 
    ('a', ''),('abc', ''), ('abba', 'abba'), ('aba', 'aba'), ('abbc', 'bb')]
for (t, expected_result) in tests: 
    s=Solution()
    print( t, s.longestPalindrome(t), expected_result)