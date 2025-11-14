"""
Title: Remove Duplicates from Sorted Array
Difficulty: Easy


Description (short): Remove duplicates from a sorted list in-place.
                     Returns the number of unique elements.

Time complexity: O(n)
Space complexity: O(1)

"""

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if not nums:  # if list is empty
            return 0

        j = 0  # j will track the index of the last unique element

        for i in range(1, len(nums)):  # start from index 1
            if nums[i] != nums[j]:  # found a new unique element
                j += 1
                nums[j] = nums[i]  # place the unique element at new position

        return j + 1  # total count of unique items


if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    sol = Solution()
    result = sol.removeDuplicates(nums)

    print("Number of unique elements:", result)
    print("Array after removing duplicates:", nums[:result])
