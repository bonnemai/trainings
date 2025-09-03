class Solution:
    def simplifyPath(self, path: str) -> str:
        path_array=path.split('/')
        new_path=[]
        for p in path_array: 
            if p in ['', '.']:
                continue
            if p in ['..', '...']: 
                if len(new_path)>0: 
                    new_path.pop()
            else:
                new_path.append(p)
        return '/'+'/'.join(new_path)
s=Solution()
tests=[
    ('/home/', '/home')
]
for (path, expected_results) in tests:
    res=s.simplifyPath(path)
    print(res==expected_results, path, res)