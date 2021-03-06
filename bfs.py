from collections import defaultdict

class graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, s):

        visited = [False]*(len(self.graph))
        queue = []
        queue.append(s);
        visited[s]=True

        while queue:
            s = queue.pop(0)
            print(s, end=" ")

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

g = graph()
g.addEdge(0,1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is the Breadth first search traversal from node(2) ")

g.bfs(2)
