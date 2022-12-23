class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i in range(len(nums)):
            another = target - nums[i]
            if another in table:
                # if table[another] != i:
                return [i, table[another]]
            table[nums[i]] = i
        return [-1, -1]