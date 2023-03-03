class Solution:
    """
    chronological order?

    미팅이 언제 시작하고 언제 끝나는 지는 중요하지 않다.

    어쨌든 어떤 미팅이 시작할 때, 빈 방이 있는지(내 앞에 상담이 끝난 방이 있는지) 이게 더 중요.

    내 원래 알고리즘도 s는 end time이랑만 비교하지 다른 거랑 비교하지 않음. 

    따라서 s와 e를 따로 모아서 정렬해놓고, 각 s가 시작할 때 끝난 e가 없으면 새로운 방, 아니면 그 방에 이어서 배정

    > When we encounter an ending event, that means that some meeting that started earlier has ended now. We are not really concerned with which meeting has ended. All we need is that **some** meeting ended thus making a room available.
    """
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        used_rooms = 0

        start_timings = sorted(interval[0] for interval in intervals)
        end_timings = sorted(interval[1] for interval in intervals)

        start_pointer = 0
        end_pointer = 0
        while start_pointer < len(intervals):
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                end_pointer += 1
            else:
                used_rooms += 1
            start_pointer += 1
        return used_rooms

    def minMeetingRooms1(self, intervals: List[List[int]]) -> int:
        end_times = [0]
        START, END = 0, 1
        intervals.sort(key=lambda x: x[START])
        for s, e in intervals:
            # 이렇게 매번 비교할 필요 없도록 우선순위 큐에 가장 빨리 끝나는 방이 먼저 나오도록 할 수 있음
            for i in range(len(end_times)):
                if s >= end_times[i]:
                    end_times[i] = e
                    break
            else:
                end_times.append(e) 
        return len(end_times)

    def minMeetingRooms2(self, intervals: List[List[int]]) -> int:
        START, END = 0, 1
        intervals.sort(key=lambda x: x[START])
        end_times = [intervals[0][1]]
        for s, e in intervals[1:]:
            if s >= end_times[0]:
                heapq.heappop(end_times)
            heapq.heappush(end_times, e)
        return len(end_times)
