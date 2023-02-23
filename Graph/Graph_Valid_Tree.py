from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = [False] * n
        parents = {0: -1}
        
        q = deque([0])
        while q:
            node = q.popleft()
            if visited[node]:
                return False
            visited[node] = True
            for neighbor in graph[node]:
                if parents[node] == neighbor:
                    continue
                parents[neighbor] = node
                q.append(neighbor)
        return all(visited[node] for node in range(n))


    def validTree4(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = [False] * n
        
        q = deque([0])
        while q:
            node = q.popleft()
            if visited[node]:
                return False
            visited[node] = True
            for neighbor in graph[node]:
                graph[neighbor].remove(node)
                q.append(neighbor)
        return all(visited[node] for node in range(n))


    def validTree3(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = [False] * n
        
        q = deque([0])
        visited[0] = True
        while q:
            node = q.popleft()
            for neighbor in graph[node]:
                if visited[neighbor]:
                    continue
                visited[neighbor] = True
                q.append(neighbor)

        return all(visited[node] for node in range(n))

    def validTree2(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = [False] * n

        def go(node):
            for neighbor in graph[node]:
                if visited[neighbor]:
                    continue
                visited[neighbor] = True
                go(neighbor)

        visited[0] = True
        go(0)

        return all(visited[node] for node in range(n))


    def validTree1(self, n: int, edges: List[List[int]]) -> bool:
        # 엣지가 n-1개를 넘어가면 무조건 사이클 생김
        if len(edges) != n-1:
            return False
        parents = [i for i in range(n)]
        sizes = [1] * n

        def find(node):
            root = node
            while parents[root] != root:
                root = parents[root]
            # 현재 노드 포함 위 노드들 모두 루트로 direct 연결
            while parents[node] != root:
                old_parent = parents[node]
                parents[node] = root
                node = old_parent
            return root

        def union(a, b):
            # 작은 쪽을 큰 쪽에 붙인다
            if sizes[a] < sizes[b]:
                parents[a] = b
                sizes[b] += sizes[a]
            else:
                parents[b] = a
                sizes[a] += sizes[b]

        for a, b in edges:
            a_root = find(a)
            b_root = find(b)
            if a_root == b_root:
                return False
            union(a_root, b_root)
        return True
