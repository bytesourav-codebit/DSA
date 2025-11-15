'''
Title: Roman to Integer
Difficulty: Easy

Description (short): Convert a Roman numeral string into its integer value,
handling subtraction rules such as IV = 4 or IX = 9.

Time complexity: O(n) — single pass through the string
Space complexity: O(1) — fixed-size mapping
'''

class Solution:
    def romanToInt(elf, s: str) -> int:
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 
        }

        result = 0

        for i in range(len(s)):

            if i+1 < len(s) and roman_to_int[s[i]] < roman_to_int[s[i+1]]:
                result -= roman_to_int[s[i]]
            
            else:
                result += roman_to_int[s[i]]

        return result
    

if __name__ == '__main__':
    s="MCMXCIV"
    sol = Solution()

    print(sol.romanToInt(s))