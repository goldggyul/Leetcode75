import collections
from typing import List


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        # adjacency matrix
        graphs = [[] for _ in range(len(vals))]
        for a, b in edges:
            graphs[b].append(a)
            graphs[a].append(b)

        # value를 기준으로 노드 정렬
        value_to_nodes = collections.defaultdict(list)
        for i, val in enumerate(vals):
            value_to_nodes[val].append(i)
        value_to_nodes = list(value_to_nodes.items())
        value_to_nodes.sort(key=lambda x: x[0])

        # 모든 노드들 기준으로 Union Find,
        # 단 조건은 내 value보다 큰 값은 연결 불가능
        number_of_good_paths = 0
        self.parents = list(i for i in range(len(vals)))
        self.rank = [0] * len(vals)
        for value, nodes in value_to_nodes:
            for node in nodes:
                for neighbor in graphs[node]:
                    if vals[neighbor] > value:
                        continue
                    self.union(node, neighbor)

            number_of_nodes_of_root = collections.defaultdict(int)
            for node in nodes:
                number_of_nodes_of_root[self.find(node)] += 1
            for _, number_of_nodes in number_of_nodes_of_root.items():
                number_of_good_paths += ((number_of_nodes + 1) * number_of_nodes) // 2

        return number_of_good_paths

    def union(self, a: int, b: int):
        a_parent = self.find(a)
        b_parent = self.find(b)
        # rank -> 자신을 루트로 하는 트리의 높이
        if self.rank[a_parent] == self.rank[b_parent]:
            self.rank[b_parent] += 1
        if self.rank[a_parent] > self.rank[b_parent]:
            a_parent, b_parent = b_parent, a_parent
        # 작은 걸 큰 쪽에 붙여준다
        self.parents[a_parent] = b_parent

    def find(self, node: int) -> int:
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]


if __name__ == '__main__':
    print(Solution().numberOfGoodPaths([1, 3, 2, 1, 3], [[0, 1], [0, 2], [2, 3], [2, 4]]))
