class Solution:
    """
    이전엔 n^2logN으로 구현했는데 시간초과가 났었다...
    구현하다가 실수를 너무 많이해서 짜증나서 다음날 풀었다

    첫번째: 맵에 저장
    중복 조심 ;;
    """

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        answer = []
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        keys = list(count.keys())
        keys.sort()
        for i in range(len(keys)):
            for j in range(i, len(keys)):
                if j == i and count[keys[i]] <= 1:
                    continue
                target = -(keys[i] + keys[j])
                if target < keys[j]:
                    continue
                countDuplicate = (1 if keys[i] == target else 0) + (1 if keys[j] == target else 0)
                if count[target] > countDuplicate:
                    answer.append([keys[i], keys[j], target])
        return answer

    """
    아니 투포인터 생각했는데 왜 n^3이라고 생각했지..?
    한 피봇을 잡고 나머지를 값을 조절해가면서 계산하면 된다.
    주의할 건 **중복**
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                numsSum = nums[i] + nums[lo] + nums[hi]
                if numsSum == 0:
                    answer.append([nums[i], nums[lo], nums[hi]])
                    # lo, hi 업데이트
                    lo += 1
                    hi -= 1
                    while lo < len(nums) - 1 and nums[lo] == nums[lo - 1]:
                        lo += 1
                    while 0 < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1
                elif numsSum < 0:
                    lo += 1
                else:
                    hi -= 1
        return answer
