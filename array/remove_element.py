'''
Title: Remove Element
Difficulty: Easy

Description (short): Remove all occurrences of a given value from the array
                     in-place. Return the number of elements that are not equal
                     to the given value.

Time complexity: O(n)
Space complexity: O(1)

'''

from typing import List

class Solution:
    def removeElements(self, nums: List[int], target: int) -> int:

        for i in range(len(nums)):
            if target in nums:
                nums.remove(target)

if __name__ == "__main__":
    nums = [10, 20, 20, 20, 30, 40]
    target = 20
    sol = Solution()
    result = sol.removeElements(nums, target)

    for i in nums:
        print(i, end=" ")