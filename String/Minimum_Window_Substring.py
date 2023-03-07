from collections import Counter

class Solution:

    """
    시간을 좀 더 줄이기 위해 s 문자열을 모두 보는 게 아니라,
    t에 있는 문자가 나올 때만 본다.

    시간 복잡도는 동일하지만 
    몇몇 케이스에선 filtered_s가 매우 작을 수가 있다.
    """

    def minWindow(self, s: str, t: str) -> str:
        dict_t = Counter(t)
        filtered_s = []
        for i, char in enumerate(s):
            if char in dict_t:
                filtered_s.append((i, char))

        ans = s + '0'
        window_counts = {}
        left, right = 0, 0
        included = 0
        while right < len(filtered_s):
            # right 포함시키기
            char = filtered_s[right][1]
            window_counts[char] = window_counts.get(char, 0) + 1
            if window_counts[char] == dict_t[char]:
                included += 1
            while left <= right and included == len(dict_t):
                char = filtered_s[left][1]
                start, end = filtered_s[left][0], filtered_s[right][0]
                if len(ans) > end - start + 1:
                    ans = s[start:end + 1]
                # left 빼기
                window_counts[char] -= 1
                if window_counts[char] < dict_t[char]:
                    included -= 1
                left += 1
            right += 1
        return ans if len(ans) <= len(s) else ""

    """
    슬라이딩 윈도우 구현 시 lo, hi의 기준을 잘 잡을 것.
    여기선 hi인 걸 포함시키고 lo인 걸 제외했다.

    맨 처음에 t에 있는 알파벳들을 Counter로 개수를 센 뒤에 s문자열에 등장하면
    -1로 개수를 빼는 식으로 구현했다. 따라서 양수인 게 있다면 아직 invalid한 것

    valid할 때까지 hi를 늘리고, valid하다면 그 때 정답을 저장

    시간/공간복잡도: S + T
    """
    def minWindow1(self, s: str, t: str) -> str:
        count = Counter(t)

        ans = s + '0'
        lo, hi = 0, 0
        while lo <= hi < len(s):
            # hi 포함시킴
            if s[hi] in count:
                count[s[hi]] -= 1
            while lo <= hi and all(value <= 0 for value in count.values()):
                if hi - lo + 1 < len(ans):
                    ans = s[lo:hi + 1]
                # lo 제외시킴
                if s[lo] in count:
                    count[s[lo]] += 1
                lo += 1
            hi += 1
        return ans if len(ans) <= len(s) else ""

            
