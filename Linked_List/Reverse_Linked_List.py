# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    2. 반복문
    좀 느리지만(시간 복잡도 동일) 메모리 덜씀
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev, curr = None, head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev, curr = curr, next_temp
        return prev

    """
    1. 재귀
    빠르지만(시간 복잡도 동일) 메모리 더 씀

    공간복잡도 O(n)
    ** 재귀로 인한 스택 공간 필요 **
    그리고 재귀는 최대 깊이 n
    """
    def get_reversed_head(self, node: Optional[ListNode], new_next: Optional[ListNode]) -> Optional[ListNode]:
        if not node.next:
            node.next = new_next
            return node
        head = self.get_reversed_head(node.next, node)
        node.next = new_next
        return head

    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        return self.get_reversed_head(head, None)