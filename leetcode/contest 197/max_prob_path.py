from collections import defaultdict
from typing import List

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # max_prob = 0.
        edge_dict = defaultdict(list)
        prob_dict = dict()
        # visited = dict()

        for edge, prob in zip(edges, succProb):
            edge_dict[edge[0]].append(tuple(edge))
            edge_dict[edge[1]].append(tuple(edge))
            prob_dict[tuple(edge)] = prob
            # visited[tuple(edge)] = False
        

        def dfs(p1, prob, max_prob, neighbors, visited):
            if len(neighbors)==0:
                return max_prob
            
            max_probs = []
            for next_edge in neighbors:
                p2 = next_edge[1]
                if p1==next_edge[1]:
                    p2 = next_edge[0]

                print(next_edge, prob)

                if prob*prob_dict[next_edge] <= max_prob:
                    return max_prob

                if p2 == end:
                    max_prob = prob*prob_dict[next_edge]
                    print(max_prob)
                    return max_prob

                neighbors = []
                for edge in edge_dict[p2]:
                    if edge[0] not in visited and edge[1] not in visited:
                        neighbors.append(edge)

                max_prob = max(max_prob, dfs(p2, prob*prob_dict[next_edge], max_prob, neighbors, visited+[p2]))
            return max_prob

        neighbors = edge_dict[start]
        return dfs(start, 1., 0., neighbors, [start])

if __name__ == "__main__":
    n = 3
    # edges = [[2,3],[1,2],[3,4],[1,3],[1,4],[0,1],[2,4],[0,4],[0,2]]
    # succProb = [0.06,0.26,0.49,0.25,0.2,0.64,0.23,0.21,0.77]
    edges = [[0,1],[1,2],[0,2]]
    succProb = [0.5,0.5,0.2]
    start = 0
    end = 2
    prob = Solution().maxProbability(n, edges, succProb, start, end)
    print(prob)