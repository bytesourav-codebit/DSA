class Solution:
    def reverseInteger(self, x: int) -> int:
        # Convert the integer to a string so we can reverse its digits easily
        s = str(x)

        # If the number is negative, skip the '-' sign (s[1:]) while reversing
        if x < 0:
            # Reverse digits only, convert back to int, and then apply the negative sign
            rev = -1 * int("".join(reversed(s[1:])))

        else:
            # For positive numbers, reverse the entire string directly
            rev = int("".join(reversed(s)))

        # Check 32-bit integer overflow (LeetCode requirement)
        # If reversed number is outside allowed range, return 0
        if rev < -2 ** 31 or rev > 2 ** 31 - 1:
            return 0

        # Return the reversed integer
        return rev
    

if __name__ == "__main__":
    x = -1256
    sol = Solution()
    print(sol.reverseInteger(x))
