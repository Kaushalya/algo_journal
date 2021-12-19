# Level: Medium
from typing import Dict, Set

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


copied_map: Dict[int, 'Node']  = dict()
visited: Set[int] = set()
    
def create_node(node:'Node'): 
    if node.val not in copied_map.keys():
        copy = Node(node.val, None)
        copied_map[node.val] = copy
    
        for nei in node.neighbors:
            create_node(nei)
    
    
def copy_node(node: 'Node')->'Node':
    # if node.val in copied_map.keys():
    #     return copied_map[node.val]
    
    if node.val in visited:
        return copied_map[node.val]
    
    visited.add(node.val)
    neighbors = [copy_node(nei) for nei in node.neighbors]
    copied_map[node.val].neighbors = neighbors

    return copied_map[node.val]
        
def copy_node_new(node: 'Node')->'Node':
    # if node.val in copied_map.keys():
    #     return copied_map[node.val]
    
    copy = Node(node.val, None)
    copied_map[node.val] = copy
    
    for nei in node.neighbors:
        if nei.val not in visited:
            visited.add(nei.val)
            copy.neighbors.append(copy_node(nei))
        else:
            copy.neighbors.append(copied_map[nei.val])

    return copy

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node==None:
            return node

        create_node(node)
        # print(copied_map.keys())
        return copy_node(node)
        
if __name__ == "__main__":
    Solution().cloneGraph(Node())
    print(Solution().cloneGraph)