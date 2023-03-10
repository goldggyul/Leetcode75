class Solution:
    """
    Constraints
    s = 1000
    최소 길이는 1

    Ideas
    어떤 문자열이 팰린드롬이라면
    그 문자열에서 시작과 끝을 제외해도 팰린드롬이다.

    이를 이용해서 가장 작은 팰린드롬부터 시작해서 긴 것까지 찾음

    각 팰린드롬 길이별 시작 인덱스를 맵에 저장해두고 찾는다.

    길이 1, 2인 팰린드롬은 초기에 넣어준다
    그리고 길이 3부터
    길이 3이라면 길이 1 팰린드롬에서 양쪽이 같으면 성립
    길이 4라면 길이 2 팰린드롬에서 양쪽이 같으면 성립
    ...
    그리고 마지막 길이에 있는 것이 정답
    이 때 홀수/짝수 길이의 시작점이 다르므로 이를 주의해야함

    시간복잡도는
    모든 길이별로 최대 모든 원소를 볼 수 있으므로 n^2
    공간복잡도는 길이별로 모든 원소가 있다면 n^2

    -> 최적화: 모든 길이에 대한 인덱스를 저장할 필요 없음

    Solution
    그냥 i부터 시작하는 팰린드롬을 그 때 그때 셈
    똑같이 n^2이지만 공간복잡도 상수
    """

    def longestPalindrome(self, s: str) -> str:

        def find_max_palindrome_start(length):
            start = []
            if length == 1:
                start = [i for i in range(len(s))]
            else:
                for i in range(len(s) - 1):
                    if s[i] == s[i + 1]:
                        start.append(i)
            while start:
                next_start = []
                for index in start:
                    if index - 1 < 0 or index + length >= len(s):
                        continue
                    if s[index - 1] == s[index + length]:
                        next_start.append(index - 1)
                if not next_start:
                    return s[start[0]:start[0] + length]
                start = next_start
                length += 2
            return ""

        # 홀수 길이 최고 찾기
        odd = find_max_palindrome_start(1)
        # 짝수 길이 최고 찾기
        even = find_max_palindrome_start(2)
        return max(odd, even, key=lambda x: len(x))

    def longestPalindrome1(self, s: str) -> str:
        start_of_length = collections.defaultdict(list)
        # 길이 1
        for i in range(len(s)):
            start_of_length[1].append(i)
        # 길이 2
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                start_of_length[2].append(i)

        def find_max_palindrome_start(length):
            while length - 2 in start_of_length:
                for index in start_of_length[length - 2]:
                    if index - 1 < 0 or index + length - 2 >= len(s):
                        continue
                    if s[index - 1] == s[index + length - 2]:
                        start_of_length[length].append(index - 1)
                length += 2

        # 홀수 길이 최고 찾기
        find_max_palindrome_start(3)
        # 짝수 길이 최고 찾기
        find_max_palindrome_start(4)
        max_length, (start, *_) = max(start_of_length.items(), key=lambda x: x[0])
        return s[start:start + max_length]

