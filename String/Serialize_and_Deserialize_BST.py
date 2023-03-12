# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 21M
class Codec:
    def encode_dfs(self, node: Optional[TreeNode], encoded: str):
        if not node:
            encoded += '-1 '
            return encoded
        encoded += str(node.val) + ' '
        encoded = self.encode_dfs(node.left, encoded)
        encoded = self.encode_dfs(node.right, encoded)
        return encoded

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        return self.encode_dfs(root, '')

    def decode_dfs(self, index: int, values: List[int]) -> Optional[TreeNode]:
        if values[index] == -1:
            return None, index
        node = TreeNode(values[index])
        node.left, index = self.decode_dfs(index + 1, values)
        node.right, index = self.decode_dfs(index + 1, values)
        return node, index

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        values = list(map(int, data.split()))
        root, _ = self.decode_dfs(0, values)
        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans