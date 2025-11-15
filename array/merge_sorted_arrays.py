'''
Title: Merge Sorted Array
Difficulty: Easy

Description (short): Merge two sorted arrays into one sorted array
in-place, with the first array having enough extra
space at the end to hold all elements.

Time complexity: O((m + n) log(m + n)) — because you sort at the end
Space complexity: O(1) — merging is done in-place

'''

from typing import List

class Solution:
    def merge(self, nums1:List[int], m: int, nums2: List[int], n: List) -> None:

        for i in range(n):
            nums1[m] = nums2[i]
            m+=1
        nums1.sort()

if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    sol = Solution()

    result = sol.merge(nums1, m, nums2, n)

    for i in range(len(nums1)):
        print(nums1[i], end = " ")