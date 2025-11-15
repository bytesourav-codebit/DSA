'''
Title: Search Insert Position
Difficulty: Easy

Description (short): Return the index of the target if found in the sorted array.
Otherwise return the index where it would be inserted
in order.

Time complexity: O(log n) — binary search
Space complexity: O(1) — constant extra space
'''

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target:int) -> int:

        low = 0
        high = len(nums) - 1

        while low <= high:

            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                low = mid + 1

            elif nums[mid] > target:
                high = mid - 1

            else:
                return low
            
if __name__ == '__main__':

    nums = [1, 3, 5, 6]
    target = 5

    sol = Solution()

    print(sol.searchInsert(nums, target))
