"""
Title: Group Anagrams
Difficulty: Medium

Description (short): Group strings that are anagrams of each other into
separate lists by using a sorted version of each
word as the key.

Time complexity: O(n · k log k) — sorting each word (k = length of word)
Space complexity: O(n · k) — storing grouped anagrams
"""
from typing import List
from collections import defaultdict
class Solution:
    def groupAnagram(self, strs: List[str]) -> List[List[str]]:

        anagram_map = defaultdict(list)
        result = []

        for s in strs:
            sorted_s = tuple(sorted(s))
            anagram_map[sorted_s].append(s)

        for value in anagram_map.values():
            result.append(value)

        return result
    
if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    sol = Solution()

    print(sol.groupAnagram(strs))