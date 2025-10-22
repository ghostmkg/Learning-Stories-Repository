# File name: learning_story_contribution.py

"""
This is a sample Python script that demonstrates a story-based approach 
to explain the Binary Tree Serialization concept with code and comments.

Binary tree serialization is a way to convert the tree structure into a string 
format to easily save/load or transmit it.

Author: YourName
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    """Encodes a tree to a single string."""
    def helper(node):
        if not node:
            return '#,'
        return str(node.val) + ',' + helper(node.left) + helper(node.right)
    return helper(root)

def deserialize(data):
    """Decodes your encoded data to tree."""
    def helper(nodes):
        val = next(nodes)
        if val == '#':
            return None
        node = TreeNode(int(val))
        node.left = helper(nodes)
        node.right = helper(nodes)
        return node

    node_iter = iter(data.split(','))
    return helper(node_iter)

# Example storytelling usage:
if __name__ == "__main__":
    # Creating a simple binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    serialized = serialize(root)
    print("Serialized tree:", serialized)

    deserialized = deserialize(serialized)
    print("Deserialization done. Root value:", deserialized.val)
