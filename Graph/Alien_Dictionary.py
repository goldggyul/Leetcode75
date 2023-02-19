from collections import deque, defaultdict


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        indegree = {c: 0 for word in words for c in word}
        outdegree = defaultdict(list)
        for before, after in zip(words, words[1:]):
            for b, a in zip(before, after):
                if b != a:
                    # 작은쪽 -> 큰쪽으로
                    if a not in outdegree[b]:
                        outdegree[b].append(a)
                        indegree[a] += 1
                    break
            # 문자가 모두 같았을 때 앞이 더 짧아야 함
            else:
                if len(before) > len(after):
                    return ""
        # 위상정렬
        q = deque([c for c in indegree if indegree[c] == 0])
        ans = []
        while q:
            letter = q.popleft()
            ans.append(letter)
            for smaller in outdegree[letter]:
                indegree[smaller] -= 1
                if indegree[smaller] == 0:
                    q.append(smaller)
        if len(ans) < len(indegree):
            return ""
        return "".join(ans)

