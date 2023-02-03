class Solution:
    """
    이걸 왜 40분이나;;

    dp 정의 잘 쓰고 구현 시작하자 ^^
    여기서 dp[i] 는 i번째까지 고려했을 때 방법
    따라서 dp[i]는
    - 만약 s[i]가 변환가능하면 dp[i-1] 개수와 같고
    - 만약 s[i-1:s+1]가 변환가능하면 dp[i-2] 개수와 같다
    dp[i] 방법이 0가지라면 이미 틀린 문자열이므로 바로 리턴한다

    생각해보면 쉬운데 실수를 너무 많이 해서 40분이 걸렸다.
    실수의 원인은
    * dp 배열의 정의를 두루뭉술하게만 생각하고 확실하게 하지 않은 탓이다.
    * 또한 i-1만 생각했지 i-2까지 참조한다는 생각을 처음에 바로 하지 못했다.
    따라서
    * dp 배열의 정의를 머릿속으로만 생각하지 말고 주석에 말로 확실하게 적고 구현
    * 정의 생각 후 i-1뿐만 아닌 i-2, i-3 등등까지 참고하는 것 생각하기
    """
    def numDecodings1(self, s: str) -> int:
        dp = [0] * len(s)
        encoded = set(str(i) for i in range(1, 27))
        if s[0] == '0':
            return 0
        def encodable(letter):
            if letter[0] == '0':
                return False
            if int(letter) > 26:
                return False
            return True
        dp[0] = 1
        for i in range(1, len(s)):
            current_valid = True if encodable(s[i]) else False
            two_valid = True if encodable(s[i-1:i+1]) else False
            if current_valid:
                dp[i] += dp[i-1] if i-1>=0 else 1
            if two_valid:
                dp[i] += dp[i-2] if i-2>=0 else 1
            if dp[i] == 0:
                return 0
        return dp[-1]

    """
    Solution
    encodable 함수 없이 숫자 범위만으로 판단 가능
    """
    def numDecodings2(self, s: str) -> int:
        dp = [0] * len(s)
        for i in range(len(s)):
            if s[i] != '0':
                dp[i] = dp[i-1] if i-1>=0 else 1
            if i > 0 and s[i-1] != '0' and 1 <= int(s[i-1:i+1]) <= 26:
                dp[i] += dp[i-2] if i-2 >=0 else 1
            if dp[i] == 0:
                return 0
        return dp[-1]

    """
    드디어 피보나치스러운 풀이를 혼자 생각했다!
    dp[i] 에서 매번 i-1, i-2번째만 참고하므로 배열 필요 없이 이전 두 방법의 개수만 알면 된다!
    Solution
    '0'으로 시작하는 지 판단할 거 없이 10보다 큰지만 보면 된다
    """
    def numDecodings(self, s: str) -> int:
        prev1, prev2 = 1, 1
        for i in range(len(s)):
            current = 0
            if s[i] != '0':
                current += prev1
            if i > 0 and 10 <= int(s[i-1:i+1]) <= 26:
                current += prev2
            if current == 0:
                return 0
            prev1, prev2 = current, prev1
        return prev1
