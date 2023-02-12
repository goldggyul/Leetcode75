"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque


class Solution:

    """
    처음에 문제 이해가 안돼서 검색하다가 map을 이용한다는 풀이를 봐버려서 ..^^;
    노드의 이웃의 이웃의 이웃... 까지 모두 만들어야 하니까 재귀로 타고 들어가게 했다.
    이 때 이미 만들어진 노드는 그냥 맵에서 찾아서 반환한다.
    ---
    난 원래 재귀로 구현했지만... dfs로도 되니까 bfs로도 될 것!
    복사본을 새로 생성할 때만 큐에 넣는다.

    이미 만들어진 걸 해쉬맵(딕셔너리)에 저장하는 게 핵심
    """
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        originals, clones = deque([node]), {node.val: Node(node.val)}
        while originals:
            original = originals.popleft()
            cur_clone = clones[original.val]
            for neighbor in original.neighbors:
                if neighbor.val not in clones:
                    clones[neighbor.val] = Node(neighbor.val)
                    originals.append(neighbor)
                cur_clone.neighbors.append(clones[neighbor.val])
        return clones[node.val]

    def cloneGraph1(self, node: 'Node') -> 'Node':
        if node is None: return None
        self.nodes = {}

        def createCopyOf(originalNode):
            if originalNode.val in self.nodes:
                return self.nodes[originalNode.val]
            node = Node(originalNode.val)
            self.nodes[node.val] = node
            for originalNeighbor in originalNode.neighbors:
                neighbor = createCopyOf(originalNeighbor)
                node.neighbors.append(neighbor)
            return node

        return createCopyOf(node)
