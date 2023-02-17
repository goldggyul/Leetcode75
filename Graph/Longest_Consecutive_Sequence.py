class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        length = defaultdict(int)
        parents = {}

        def find_parent(num):
            if num not in parents:
                return num
            parents[num] = find_parent(parents[num])
            return parents[num]

        # 작은 쪽으로 합친다
        def merge(lo, hi):
            lo = find_parent(lo)
            hi = find_parent(hi)
            if lo == hi:
                return length[lo]
            parents[hi] = lo
            length[lo] += length[hi]
            return length[lo]

        ans = 1

        for num in nums:
            if length[num] > 0:
                continue
            length[num] = 1
            if length[num - 1] > 0:
                ans = max(merge(num - 1, num), ans)
            if length[num + 1] > 0:
                ans = max(merge(num, num + 1), ans)

        return ans

    def longestConsecutive2(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        for num in nums:
            if num - 1 in nums:
                continue
            cur = num
            consecutive = 0
            while cur in nums:
                consecutive += 1
                cur += 1
            ans = max(ans, consecutive)
        return ans

    def longestConsecutive1(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        nums.sort()
        ans = 1
        consecutive = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            if nums[i] == nums[i - 1] + 1:
                consecutive += 1
                ans = max(ans, consecutive)
            else:
                consecutive = 1
        return ans

