def has_no_duplicate(s:str):
    return len(set(s))==len(s)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        # Use sliding window with a set to track characters
        char_set = set()
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            # If we encounter a duplicate character, move left pointer
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Add current character to set
            char_set.add(s[right])
            
            # Update max length
            max_length = max(max_length, right - left + 1)
        
        return max_length

if __name__=='__main__':
    # Create a long string with all unique characters
    long_test = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ " * 100
    very_long_test = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ " * 1000
    
    solution = Solution()
    tests = [
        ('abc', 3),        
        ('abcabcbb', 3),
        ('pwwkew', 3),
        ('', 0),
        ('a', 1),
        ('aa', 1),
        ('ab', 2)
    ]
    
    print("Testing short strings:")
    for (s, expected_results) in tests: 
        result = solution.lengthOfLongestSubstring(s)
        print(f"'{s}' -> {result} (expected: {expected_results})")
    
    print(f"\nTesting long string (length: {len(long_test)}):")
    import time
    start_time = time.time()
    result = solution.lengthOfLongestSubstring(long_test)
    end_time = time.time()
    print(f"Long string result: {result}")
    print(f"Time taken: {end_time - start_time:.4f} seconds")
    
    print(f"\nTesting very long string (length: {len(very_long_test)}):")
    start_time = time.time()
    result = solution.lengthOfLongestSubstring(very_long_test)
    end_time = time.time()
    print(f"Very long string result: {result}")
    print(f"Time taken: {end_time - start_time:.4f} seconds")