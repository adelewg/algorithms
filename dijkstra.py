from queue import PriorityQueue

class Graph:

    # edges is a matrix and the size of the matrix depends on the number of vertices
    def __init__(self, numOfVertices):
        self.v = numOfVertices
        self.visited = []
        self.edges = [[-1 for i in range(numOfVertices)] for j in range(numOfVertices)]

    def addEdge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight
    

    def dijkstra(self, start_vertex):
        D = {v:float('inf') for v in range(self.v)}
        D[start_vertex] = 0

        pq = PriorityQueue()
        pq.put((0, start_vertex))

        while not pq.empty():
            (dist, current_vertex) = pq.get()
            self.visited.append(current_vertex)

