class Solution:
    """
    처음에 풀었던..
    정답이긴 한데 런타임 맨끝 메모리 맨끝에 걸린다
    될까 말까 긴가민가했는데 이미 검사한 단어를 set에 저장해서 괜찮지않을까 생각하고 풀었다

    O(n^3)?
    """
    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:
        self.wordSet = {}
        for word in wordDict:
            self.wordSet[word] = True
        def go(word):
            if word in self.wordSet:
                return self.wordSet[word]
            for i in range(1, len(word)):
                left = word[:i]
                right = word[i:]
                # print(f"left: {left} right: {right}")
                if go(left) and go(right):
                    self.wordSet[word] = True
                    return True
            self.wordSet[word] = False
        return go(s)


    """
    이걸 왜 처음에 생각 못했지?
    블로그 풀이를 다 본건 아니지만 방법을 살짝 읽고 구현했다 ㅎㅎ..
    이것도 LCS처럼 이분탐색인데
    루프 한번에 한 토막씩 보는데 그 토막 바로 전까지가 모두 가능할 때만 그 토막을 보는 방식이다.
    따라서 모두 가능하다면 맨 마지막이 True일 것.

    굳이 내가 처음에 풀었던 방식처럼 다 set으로 저장하지 않아도
    어떤 지점까지 가능하면 그냥 True로 배열에 저장하는 것이다...

    어떻게 하면 다음에 이런 생각을 할 수 있었을까?
    dp니까 배열에 어떤 상태를 저장할 지 생각해보면..
    만약 문자의 i번째 인덱스부터 체크한다면?
    그 전까지 가능했는지 정보를 저장해두면 된다.
    그리고 가능하다면 그 i부터 가능한 곳까지 또 저장해두고,
    그 가능한 곳에서 반복하면 되는 것...

    dp
    1. i번째 인덱스부터 확인하고 싶다면 그 전에 무엇이 저장되어 있어야 할까?
    2. 그럼 그걸 바탕으로 난 뭘 저장할까?
    
    O(n^3)이다!!! 루프가 n^2이지만 substring 연산을 까먹지 말자.
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        if s in wordSet:
            return True
        canSeparated = [False] * len(s)
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if i -1 >= 0 and not canSeparated[i-1]:
                    continue
                subString = s[i:j]
                if subString in wordSet:
                    canSeparated[j-1] = True
        return canSeparated[len(s) - 1]