"""
Title: Length of Last Word
Difficulty: Easy

Description (short): Return the length of the last word in the string
after trimming trailing spaces. Words are separated
by spaces.

Time complexity: O(n) — scanning + splitting
Space complexity: O(n) — storing split words
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()

        if not words:
            return 0
        
        return len(words[-1])
    
if __name__ == "__main__":
    s = "Hello World"
    sol = Solution()
    
    print(sol.lengthOfLastWord(s))