class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            picked = nums[i]
            another = target - picked
            if another in nums:
                another_index = nums.index(another)
                if another_index != i:
                    return [i, another_index]
        return [-1, -1]