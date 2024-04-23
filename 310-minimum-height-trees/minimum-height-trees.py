class Solution:
  def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    # Edge case: n=1, return [0]
    if n == 1:
        return [0]
    
    # Build adjacency list for the graph
    adj_list = {i: set() for i in range(n)}
    for u, v in edges:
        adj_list[u].add(v)
        adj_list[v].add(u)
    
    # Find all leaf nodes (i.e., nodes with degree 1)
    leaves = [i for i in range(n) if len(adj_list[i]) == 1]
    
    # Repeat until we are left with 1 or 2 nodes
    while n > 2:
        
        # Remove the current leaf nodes along with their edges
        n -= len(leaves)
        new_leaves = []
        for leaf in leaves:
            neighbor = adj_list[leaf].pop()
            adj_list[neighbor].remove(leaf)
            
            # If the neighbor becomes a new leaf node, add it to the list
            if len(adj_list[neighbor]) == 1:
                new_leaves.append(neighbor)
        
        # Update the list of leaf nodes
        leaves = new_leaves
    
    # The remaining nodes are the roots of the MHTs
    return leaves