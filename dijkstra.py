import sys

from collections import defaultdict
import heapq as heap


def dijkstra(AM, startingNode):
  G = AM.graph
  V = AM.V
  visited = set()
  parentsMap = {}
  pq = []
  nodeCosts = defaultdict(lambda: float('inf'))
  nodeCosts[startingNode] = 0
  heap.heappush(pq, (0, startingNode))

  while pq:
    # go greedily by always extending the shorter cost nodes first
    _, node = heap.heappop(pq)
    visited.add(node)
    # print(node, G[node])
    for adjNode, weight in G[node]:
      if adjNode in visited:	continue
        
      newCost = nodeCosts[node] + weight
      if nodeCosts[adjNode] > newCost:
        parentsMap[adjNode] = node
        nodeCosts[adjNode] = newCost
        heap.heappush(pq, (newCost, adjNode))
        
  # return [parentsMap, nodeCosts]
  results = []
  for i in range(1, V):
    results.append([parentsMap[i], i, nodeCosts[i]])
  return results


