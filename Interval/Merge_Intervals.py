class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        START, END = 0, 1
        # 문제에서 정렬됐다는 말 없음에 주의할 것
        intervals.sort()
        # 굳이 cur를 따로 저장하지 않아도 배열의 마지막과만 비교하면 된다.
        merged = [intervals[0]]
        for interval in intervals[1:]:
            if interval[START] <= merged[-1][END]:
                merged[-1][START] = min(interval[START], merged[-1][START])
                merged[-1][END] = max(interval[END], merged[-1][END])
            else:
                merged.append(interval)
        return merged

    def merge1(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        START, END = 0, 1
        # 문제에서 정렬됐다는 말 없음에 주의할 것
        intervals.sort()
        cur = intervals[0]
        for interval in intervals[1:]:
            if interval[START] <= cur[END]:
                cur[START] = min(interval[START], cur[START])
                cur[END] = max(interval[END], cur[END])
                continue 
            ans.append(cur)
            cur = interval
        ans.append(cur)
        return ans
