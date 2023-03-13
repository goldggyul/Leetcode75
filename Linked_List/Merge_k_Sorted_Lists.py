# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
priority queue는 unique한 값이 나올 때까지 tuple을 계속 비교
이 때 ListNode는 비교할 수가 없어 에러
1. tuple로 id()값을 넣어주거나
2. 아래처럼 Wrapper클래스 만들고 __lt__구현
"""


class Wrapper:
    def __init__(self, node: Optional[ListNode]):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val


class Solution:
    """
    Solution - Merge with Divide And Conquer

    * 리스트 합칠 때 새로 합치는 리스트의 head를 굳이 따로 초기화하지말고
      아무 값의 head로 만들어놓고 최종 리스트 구할때는 head.next를 반환하면 됨
    """

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2Lists(list1, list2):
            head = pointer = ListNode(0)
            while list1 and list2:
                if list1.val < list2.val:
                    pointer.next = list1
                    list1 = list1.next
                else:
                    pointer.next = list2
                    list2 = list2.next
                pointer = pointer.next

            pointer.next = list1 if list1 else list2
            return head.next

        interval = 1
        # 0,1 -> 0 | 2,3 -> 2 // 0,2 -> 4
        while interval < len(lists):
            for i in range(interval, len(lists), interval * 2):
                lists[i - interval] = merge2Lists(lists[i - interval], lists[i])
            interval *= 2

        return lists[0] if lists else None

    def mergeKLists2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        for li in lists:
            if not li:
                continue
            heapq.heappush(pq, Wrapper(li))

        head, pointer = None, None
        while pq:
            wrapper = heapq.heappop(pq)
            node = wrapper.node
            if not head:
                head = node
                pointer = head
                node = node.next
            else:
                pointer.next = node
                node = node.next
                pointer = pointer.next
            if node:
                heapq.heappush(pq, Wrapper(node))
        return head

    """
    1. Constraints
    리스트의 개수는 10^4
    각 리스트의 길이는 500

    2. Idea
    1) 최솟값 비교시 그냥 다 보기
    500 * 10^4 (최솟값을 그냥 하나씩 비교할 경우)
    2) 최솟값 비교시 priority queue 이용하기
    500 * log10^4
    2번으로 구현
    공간복잡도는 O(k)

    9M
    """

    def mergeKLists1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        for li in lists:
            if not li:
                continue
            heapq.heappush(pq, (li.val, id(li), li))

        head, pointer = None, None
        while pq:
            value, _, li = heapq.heappop(pq)
            if not head:
                head = li
                pointer = head
                li = li.next
            else:
                pointer.next = li
                li = li.next
                pointer = pointer.next
            if li:
                heapq.heappush(pq, (li.val, id(li), li))
        return head
