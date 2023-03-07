from collections import Counter

class Solution:
    """
    Solution *****
    각 문자를 정렬 후 튜플로 바꿔서 튜플을 키로 하고 문자열을 value로 해서 ans에 넣는다
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

    """
    Solution
    각 문자를 count 후에 count 배열을 **튜플**로 바꿔서 위 Solution과 같은 로직으로 구현한다. 
    """
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for i in range(len(strs)):
            target = strs[i]
            count = [0]*26
            for char in target:
                count[ord(char)-ord('a')] += 1
            ans[tuple(count)].append(target)
        return ans.values()

    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        strs.sort(key=lambda x: len(x))
        included = [False] * len(strs)
        counters = [[0]*26 for _ in range(len(strs))]
        for i, word in enumerate(strs):
            for char in word:
                counters[i][ord(char)-ord('a')] += 1
        ans = []
        for i in range(len(strs)):
            if included[i]: 
                continue
            included[i] = True            

            target = strs[i]
            ans.append([target])
            for j in range(i+1, len(strs)):
                if len(strs[j]) > len(target):
                    break
                if included[j]:
                    continue
                if counters[i] != counters[j]:
                    continue
                ans[-1].append(strs[j])
                included[j] = True
        return ans
