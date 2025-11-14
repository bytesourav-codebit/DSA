'''
Title: Two Sum
Difficulty: Easy

Description (short): Find two numbers in the list that add up to the target.
                     Return their indices (any order).

Time complexity: O(n)
Space complexity: O(n)

'''

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target) -> int:

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i,j]

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 18
    sol = Solution()
    result = sol.twoSum(nums, target)

    print(result)