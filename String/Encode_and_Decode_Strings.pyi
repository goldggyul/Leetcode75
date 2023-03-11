"""
마치 네트워크 계층에서 각 계층의 데이터의 정보를
헤더로 붙이는 것처럼, 그리고 헤더에서 데이터의 길이를 저장하는 것처럼
여기서도 각 문자열의 길이를 헤더로 붙인다.
단, 역시 헤더는 고정 길이여야 함


풀어볼 참고 문제
https://leetcode.com/problems/serialize-and-deserialize-bst/description/
"""


class Codec:
    def __init__(self):
        self.header_length = 3

    def get_length(self, word: str):
        length = str(len(word))
        return "0" * (self.header_length - len(length)) + length

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return ''.join(self.get_length(word) + word for word in strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded = []
        pointer = 0
        while pointer < len(s):
            length = int(s[pointer:pointer + self.header_length])
            word = s[pointer + self.header_length: pointer + self.header_length + length]
            decoded.append(word)
            pointer = pointer + self.header_length + length
        return decoded


class Codec1:
    def __init__(self):
        self.separator_count = 1
        self.separator = ' '

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        for word in strs:
            # count a number of consecutive separators
            pointer = 0
            while pointer < len(word):
                if word[pointer] != self.separator:
                    pointer += 1
                    continue
                next_pointer = pointer
                while next_pointer < len(word) and word[next_pointer] == self.separator:
                    next_pointer += 1
                separator_count = next_pointer - pointer
                self.separator_count = max(separator_count + 1, self.separator_count)
                pointer = next_pointer
        return (self.separator * self.separator_count + '\n').join(strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        return s.split(self.separator * self.separator_count + '\n')

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
