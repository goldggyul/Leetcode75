# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    """
    Solution: 플로이드 순환 찾기 알고리즘 Floyd's Cycle Finding Algorithm

    만약 달리기 경주에서, 트랙이 일자 트랙이 아니라 원형 트랙(사이클이 있는)을 계속 돈다면
    두 선수의 달리기 속도가 차이나면 어떻게 될까?
    더 빠른 선수가 느린 선수를 만날 것이다.

    따라서 이 문제에서 더 빠른 선수(pointer)가 결승점에 도달하기 전에 더 느린 선수를 만나는 지 여부로
    사이클 여부를 판단할 수 있다
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow, fast = head, head.next
        while slow != fast:
            # fast runner가 먼저 도달 -> cycle 없음
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True


    def hasCycle1(self, head: Optional[ListNode]) -> bool:
        curr = head
        visited = set()
        while curr:
            if curr in visited:
                return True
            visited.add(curr)
            curr = curr.next
        return False
