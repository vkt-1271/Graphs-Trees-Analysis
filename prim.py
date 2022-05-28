import sys

def prim2(G,N):
  INF = sys.maxsize
  selected_node = [0] * N
  no_edge = 0
  selected_node[0] = True
  result = []

  while (no_edge < N - 1):
      minimum = INF
      a = 0
      b = 0
      for m in range(N):
          if selected_node[m]:
              for n in range(N):
                  if ((not selected_node[n]) and G[m][n]):  
                      if minimum > G[m][n]:
                          minimum = G[m][n]
                          a = m
                          b = n
      result.append([a, b, G[a][b]])
      selected_node[b] = True
      no_edge += 1
  return result