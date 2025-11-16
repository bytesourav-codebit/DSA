"""
Title: Valid Palindrome
Difficulty: Easy

Description (short): Determine if a string is a palindrome after converting
all letters to lowercase and removing all non-alphanumeric
characters.

Time complexity: O(n) — single pass to clean + reverse check
Space complexity: O(n) — cleaned string storage
"""

class Solution:
    def isPalindrome(self, s:str) -> bool:
        new = ""
        for i in s:
            if i.isalnum():
                new += i.lower()
            return new == new[::-1]
        
if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    sol = Solution()

    print(sol.isPalindrome(s))