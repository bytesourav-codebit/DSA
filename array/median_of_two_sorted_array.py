
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = []

        nums3.extend(nums1)
        nums3.extend(nums2)

        nums3.sort()

        length = len(nums3)

        if length % 2 == 0:
            mid = length // 2 - 1
            mid2 = length // 2
            median = (nums3[mid] + nums3[mid2]) / 2
        else:
            mid = length // 2
            median = nums3[mid]

        return median
    
if __name__ == "__main__":
    nums1 = [1, 3]
    nums2 = [2, 4]

    sol = Solution()

    print(sol.findMedianSortedArrays(nums1, nums2))
