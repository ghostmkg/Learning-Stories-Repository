"""
Learning Story: Binary Tree Serialization

This script demonstrates how to serialize (convert to string) and deserialize (reconstruct) a binary tree in Python.
It includes step-by-step documentation to guide learners through recursive approach and data structure handling.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string."""
        def recur(node):
            if not node:
                vals.append('null')
                return
            vals.append(str(node.val))
            recur(node.left)
            recur(node.right)

        vals = []
        recur(root)
        return ','.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        def recur():
            if self.vals[0] == 'null':
                self.vals.pop(0)
                return None
            node = TreeNode(int(self.vals[0]))
            self.vals.pop(0)
            node.left = recur()
            node.right = recur()
            return node

        self.vals = data.split(',')
        return recur()

# Demo usage:
# Build binary tree:      1
#                       /   \
#                      2     3
#                           / \
#                          4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

codec = Codec()
s = codec.serialize(root)
print("Serialized:", s)
new_root = codec.deserialize(s)
