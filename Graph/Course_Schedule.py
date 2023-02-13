class Solution:

    """
    27M
    예전에 위상정렬을 푼 적이 있어서 잠깐 생각하고 풀었다

    위상정렬 시간복잡도는 O(V+E)
    모든 노드를 확인하면서 해당 노드에서 출발하는 엣지를 확인한다
    indegree와 outdegree를 나눠서 잘 구하기!

    - dict말고 그냥 인접리스트처럼 표현할 수도 있다
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # in 배열에 수강 조건 과목 개수
        in_counts = [0] * numCourses
        # out dictionary에 각 과목을 들으면 들을 수 있는 과목 명시
        out_courses = defaultdict(list)
        # 큐에는 현재 수강할 수 있는 과목
        q = deque()
        for req in prerequisites:
            in_counts[req[0]] += 1
            out_courses[req[1]].append(req[0])
        for course in range(numCourses):
            if in_counts[course] == 0:
                q.append(course)
        while q:
            cur = q.popleft()
            for next_course in out_courses[cur]:
                if in_counts[next_course] > 0:
                    in_counts[next_course] -= 1
                    if in_counts[next_course] == 0:
                        q.append(next_course)
        # 수강할 수 있는 과목을 다 돌았는데 in 배열에 0이 아닌 과목이 있다면 수강 불가
        return all(count == 0 for count in in_counts)

