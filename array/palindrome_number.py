

class Solution:
    def palindromeNumber(self, x: int) -> int:
        if x < 0:
            return False
        
        reverse = 0
        xcopy = x

        while x > 0:
            reverse = (reverse * 10) + (x % 10)
            x //= 10

        return reverse == xcopy
    
if __name__ == "__main__":
    x = 121
    sol = Solution()

    print(sol.palindromeNumber(x))
