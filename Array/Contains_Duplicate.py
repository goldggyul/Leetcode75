"""
https://leetcode.com/problems/contains-duplicate/description/
2M
"""


class Solution:
    # O(NlogN)
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                return True
        return False

    # hash set이므로 O(N)
    def containsDuplicate2(self, nums: List[int]) -> bool:
        nums_set = set([])
        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num)
        return False
