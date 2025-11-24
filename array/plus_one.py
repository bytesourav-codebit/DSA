
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        length = len(digits)
        num = 0

        for i in range(length - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            digits[i] = 0

        return [1] + digits
    
if __name__ == "__main__":
    digits = [9, 9, 9]
    sol = Solution()

    print(sol.plusOne(digits))