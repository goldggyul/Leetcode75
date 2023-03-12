# https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/

class Trie:
    def __init__(self):
        self.visited = 0
        self.children: List[Optional[Trie]] = [None] * 26


class Solution:

    """
    Solution

    Trie 이용하기
    """

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = Trie()
        for word in words:
            trie = root
            for letter in word:
                letter = ord(letter) - ord('a')
                if trie.children[letter] is None:
                    trie.children[letter] = Trie()
                trie.children[letter].visited += 1
                trie = trie.children[letter]

        score = [0] * len(words)
        for i, word in enumerate(words):
            trie = root
            for j, letter in enumerate(word):
                letter = ord(letter) - ord('a')
                cur_visited = trie.children[letter].visited
                if cur_visited == 1:
                    score[i] += len(word) - j
                    break
                score[i] += cur_visited
                trie = trie.children[letter]
        return score

    def sumPrefixScores1(self, words: List[str]) -> List[int]:
        prefix_count = collections.defaultdict(int)
        for word in words:
            for i in range(1, len(word) + 1):
                prefix_count[word[:i]] += 1
        count_per_word = [0] * len(words)
        for i, word in enumerate(words):
            for j in range(1, len(word) + 1):
                count_per_word[i] += prefix_count[word[:j]]
        return count_per_word