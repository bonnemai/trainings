
def is_valid(s): 
    left=0
    right=len(s)-1
    while left<right: 
        if s[left]==')': 
            return False
        if s[right]=='(': 
            return False
        left+=1
        right+=1

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Ideas: dynamic programming
        if s=='': 
            return 0
        for i in range(len(s)): 
            for j in range(i, len(s)): 
                if is_valid(s[i:len(s)-j-1]): 
                    return len(s)-j-1-i
        return 0

tests=[
    ("(()", 2),
    (")()())", 4),
    ("", 0),
    ("(()", 2),
    (")()())", 4),
]
for s, expected_results in tests:
    # print(s, expected_results)
    res=Solution().longestValidParentheses(s)
    print(res==expected_results, res)