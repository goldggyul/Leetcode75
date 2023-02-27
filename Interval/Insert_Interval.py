class Solution:
    """
    문제 입력이 이미 정렬되어 있다.
    새로운 인터벌과 영향을 주지 않는 애들은 빼고 생각한다. (left, right)
    그리고 영향을 주는 애들 중에서도 가장 왼쪽과 가장 오른쪽만 확인하면 된다. 그 사이는 어차피 정렬되어 있으니까
    그리고 그 둘과 시작, 끝만 비교하면 끝
    -> 답에 영향을 주는 게 뭔지 생각할 것, 생각하지 않아도 되는 것들 제외하고 생각하기

     1     2      3     4      5
    <-->  <---> <---> <---> <---->
            <----------->           newInterval

    1, 5는 생각하지 않아도 되고, 겹치는 건 2, 3, 4지만 어차피 인터벌에 모두 포함되므로 2, 4만 신경쓰면 된다.
    """
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval
        left = [interval for interval in intervals if interval[1] < s]
        right = [interval for interval in intervals if interval[0] > e]
        if left + right != intervals:
            s = min(s, intervals[len(left)][0])
            # e = max(e, intervals[~len(right)][1])
            # ~는 모든 비트 반전.
            # a가 있을 때 -a는 a의 모든 비트 반전 + 1(2의 보수) 이므로
            # -a = ~a + 1
            # -a-1 = ~a
            e = max(e, intervals[-len(right)-1][1])
        return left + [[s, e]] + right
        

    def insert2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = [], []
        new_start, new_end = newInterval
        for interval in intervals:
            if interval[1] < new_start:
                left.append(interval)
            elif interval[0] > new_end:
                right.append(interval)
            else:
                new_start = min(new_start, interval[0])
                new_end = max(new_end, interval[1])
        return left + [[new_start, new_end]] + right

    def insert1(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0: return [newInterval]
        to = [-1] * (max(intervals[-1][-1], newInterval[-1]) + 1)
        for start, end in intervals:
            for i in range(start, end + 1):
                to[i] = start

        pointer = newInterval[0]
        new_start = pointer
        if to[new_start] != -1:
            new_start = to[new_start]
        while pointer <= newInterval[1]:
            if to[pointer] == -1:
                to[pointer] = new_start
                pointer += 1 
            else:
                if to[pointer] > new_start:
                    target_value = to[pointer]
                    while pointer < len(to) and to[pointer] == target_value:
                        to[pointer] = new_start
                        pointer += 1
                else:
                    pointer += 1
        ans = []
        pointer = 0
        while pointer < len(to):
            if to[pointer] == -1:
                pointer += 1
                continue
            current_start = pointer
            while pointer < len(to) and to[current_start] == to[pointer]:
                pointer += 1
            ans.append([current_start, pointer - 1])
        return ans
