"""
https://leetcode.com/problems/product-of-array-except-self/
9M
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        모든 곱을 곱해놓고 나누는 식으로 하면,
        0같은 경우 divided by zero로 문제가 생긴다.
        따라서 prefix sum처럼 prefix product로 왼쪽 출발 / 오른쪽 출발을 구한다
        pre[i] = 0~i까지의 곱
        suf[i] = i ~ i-n까지의 곱
        따라서 정답은 pre[i-1] * suf[i+1]
        """
        pre = [1] * len(nums)
        suf = [1] * len(nums)
        pre[0] = nums[0]
        suf[-1] = nums[-1]
        for i in range(1, len(nums)):
            pre[i] = pre[i - 1] * nums[i]
        for i in range(len(nums) - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i]
        product_except = [0] * len(nums)
        for i in range(len(nums)):
            L = pre[i - 1] if i - 1 >= 0 else 1
            R = suf[i + 1] if i + 1 <= len(nums) - 1 else 1
            product_except[i] = L * R
        return product_except

    """
    왼쪽에서 훑으면서 한 번 곱하고,
    오른쪽에서 나머지 훑는다.
    
    이 때, 왼쪽에서 한 번 훑을 때는
    product_except[i]가 i를 제외한 왼쪽 곱이 있으므로 상관 없지만,
    오른쪽에서 훑을때는 product_except에 값이 이미 반영됐으므로
    오른쪽에서 곱하는 다른 변수를 따로 두고, 해당 값을 i에 곱해주고,
    다음을 위해 해당 변수에 i값을 다시 곱한다.
    
    Numbers:     2    3    4     5
    Lefts:       1    2  2*3 2*3*4
      *
    Rights:  3*4*5  4*5    5     1
    """

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        N = len(nums)
        product_except = [1] * N
        for i in range(1, N):
            product_except[i] = product_except[i - 1] * nums[i - 1]
        suffix = nums[-1]
        for i in range(N - 2, -1, -1):
            product_except[i] *= suffix
            suffix *= nums[i]
        return product_except
