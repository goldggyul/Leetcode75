class Solution:
    """
    요소가 작아지는 걸 최소로 찾으려면 O(n)이 걸린다.
    하지만 O(logN)을 이용해야하므로 이분탐색을 생각해볼 수 있다.

    18M
    """

    def findMin1(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[lo] < min(nums[hi], nums[mid]):
                hi = mid - 1
            elif nums[hi] < min(nums[lo], nums[mid]):
                lo = mid + 1
            elif nums[mid] <= min(nums[lo], nums[hi]):  # mid가 가장 작을 때 and mid와 lo가 같을 때(크기가 2일 때)
                hi = mid
        return nums[hi]

    """
    Solution
    
    살짝 관점을 다르게 해서
    mid가 정답인지를 확인한다.
    10 -> 1 : 작아지면 거기가 정답
    위 사실을 이용한다.
    그리고 왼쪽/오른쪽 어디로 좁혀질 지는
    일단 0번째가 mid보다 크면 왼쪽에 답이 있다.
    만약 mid보다 작으면(같다면 이미 위에서 정답이 됐을 것)
    1 2 3 4 5같은 경우는 이미 정답으로 반복문 위에서 처리했기때문에 (이 경우를 미리 안해주면 에러!)
    2 3 4 5 1 같은 경우만 남아있다
    따라서 오른쪽으로 좁히면 된다.
    """

    def findMin2(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        lo, hi = 0, len(nums) - 1
        if nums[hi] > nums[0]:  # already sorted
            return nums[0]
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[0] > nums[mid]:
                hi = mid - 1
            elif nums[0] < nums[mid]:
                lo = mid + 1

    """
    Solution

    holy shit
    이렇게 짧게 ^^... 이분탐색은 mid와 lo hi 관계 생각하기..
    """

    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        # DO NOT use left <= right because that would loop forever
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:  # nums[mid] <= nums[hi] <- mid가 답일 수도 있음
                hi = mid
        return nums[lo]
