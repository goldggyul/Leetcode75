from collections import deque

"""
13M
"""
class Solution:
    # union find
    def countComponents1(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]

        def find(node):
            root = node
            while parents[root] != root:
                root = parents[root]
            while parents[node] != root:
                old_parent = parents[node]
                parents[node] = root
                node = old_parent
            return root

        for a, b in edges:
            a_root = find(a)
            b_root = find(b)
            parents[a_root] = b_root

        return sum(parents[node] == node for node in range(n))

    # dfs bfs
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False] * n
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def bfs(node):
            q = deque([node])
            visited[node] = True
            while q:
                cur = q.popleft()
                for neighbor in graph[cur]:
                    if visited[neighbor]:
                        continue
                    visited[neighbor] = True
                    q.append(neighbor)

        components = 0
        for node in range(n):
            if visited[node]:
                continue
            components += 1
            bfs(node)
        return components
