class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0]))
        count = 0       
        last_end = intervals[0][-1]
        for s, e in intervals[1:]:
            if s >= last_end:
                last_end = e
            else:
                last_end = min(e, last_end)
                # 이을 수 없다는 거 == 겹친다는 것이므로 이 때 겹치는 개수 세도 됨
                count += 1
        return count

    def eraseOverlapIntervals1(self, intervals: List[List[int]]) -> int:
        # lambda가 없어도 첫번째 기준으로 정렬 되지만,
        # lambda가 없으면 (x[0], x[1]) 즉 0번째가 같은 경우 1번째까지 정렬해버리므로
        # 0번째만 기준으로 정렬하게 하는 게 더 빠르다.
        intervals.sort(key=lambda x: (x[0]))
        # 안겹치고 최대 몇개 가능인지 구하고 빼면 됨 
        count = 1       
        last_end = intervals[0][-1]
        for s, e in intervals[1:]:
            if s >= last_end:
                count += 1
                last_end = e
            else:
                last_end = min(e, last_end)
        return len(intervals) - count

