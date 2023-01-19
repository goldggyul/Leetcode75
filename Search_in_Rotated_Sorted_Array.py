class Solution:
    """
    https://leetcode.com/problems/search-in-rotated-sorted-array/

    왼쪽이 정렬된 상태라면 오른쪽이 아닐 것이고,
    오른쪽이 정렬된 상태라면 왼쪽이 아닐 것.

    따라서 정렬된 쪽을 찾고 그쪽으로 보낼 수 있다면 보내고 아니면 반대로 보낸다

    ! 주의
    이분 탐색일 때 항상 사이즈 2일때 어떻게 될 지 생각하기
    이 문제의 경우엔
    [1, 3]이나 [3, 1] 생각해보기
    """

    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            if nums[lo] <= nums[mid]:  # 왼쪽 정상적 + 사이즈 2일때를 위해 등호
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return lo if nums[lo] == target else -1
