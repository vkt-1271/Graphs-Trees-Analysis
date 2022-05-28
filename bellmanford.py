def BellmanFord(AM, src):
        dist = [float("Inf")] * AM.V
        dist[src] = 0
        for _ in range(AM.V - 1):
            for u, v, w in AM.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
        for u, v, w in AM.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                        print("Graph contains negative weight cycle")
                        return
                         
        result = []
        for i in range(1, AM.V):
                result.append([0, i, dist[i]])
        return result
