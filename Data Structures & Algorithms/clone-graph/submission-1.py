"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashmap = {}

        def dfs(node):
            if not node.neighbors:
                hashmap[node.val] = Node(node.val)
                return hashmap[node.val]
            hashmap[node.val] = Node(node.val)
            neighbors = [dfs(neighbor) if neighbor.val not in hashmap else hashmap[neighbor.val] for neighbor in node.neighbors]
            hashmap[node.val].neighbors = neighbors
            return hashmap[node.val]

        return dfs(node) if node else None