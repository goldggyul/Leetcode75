class Solution:
    """
    n은 10^4

    공간 복잡도: O(1)
    시간 복잡도: O(n)

    그냥 O(n)에 할 수 있는 방법은
    처음부터 끝까지 보면서 boolean 배열 보기
    이걸 배열대신 공간복잡도를 줄이려면 비트로 저장할 수 있는데
    n이 10^4이므로 비트론 어렵다

    만약 O(n^2)으로 한다면 하나의 목표 변수를 찾는 식으로 하면 O(1)만에 할 수 있다

    그럼 하나의 변수에 나타내기 위해 뭔가 신기하게 더하는 방법은 없을까라고 생각했는데
    생각해보니까 그럼 0부터 n까지 모두 더하고 nums에 있는 걸 빼면 남은게 부족한 변수다
    """

    def missingNumberMine(self, nums: List[int]) -> int:
        allAdded = 0
        for num in range(0, len(nums)+1):
            allAdded += num
        for num in nums:
            allAdded -= num
        return allAdded


    """
    a number XOR itself will become 0, any number XOR with 0 will stay unchanged. 
    So if every number from 1...n XOR with itself except the missing number, the result will be the missing number

    그러니까
    n ^ n = 0이다.
    n ^ 0 = n이다
    그러니 만약 1부터 n까지 xor한다면 없는 숫자만 남을 것이다
    xor로 신기한 일을 하는 게 많다~
    
    (n ^ 0 = n이므로 0 + n = 0 ^ n)
    
    아래 함수가 가장 빠르고 메모리도 덜 쓰는 걸로 나왔다.
    """
    def missingNumber1(self, nums: List[int]) -> int:
        allAdded = 0
        for i in range(0, len(nums)+1):
            allAdded ^= i
        for num in nums:
            allAdded ^= num
        return allAdded

    def missingNumber(self, nums: List[int]) -> int:
        allAdded = len(nums)
        for i in range(len(nums)):
            allAdded ^= i
            allAdded ^= nums[i]
        return allAdded