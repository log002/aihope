# Kruskal's algorithm in Python


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Search function

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    #  Applying Kruskal algorithm
    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))



v=int(input("Enter the no of vertices"))
g = Graph(v)



e=int(input("Enter the no of edges"))

i=0


while i<e:
    print("Enter the edge ",i+1)
    u=int(input())
    v=int(input())
    w=int(input())
    g.add_edge(u,v,w)
    
    i=i+1

g.kruskal_algo()



# sample input and output
# Enter the no of vertices4
# Enter the no of edges5
# Enter the edge  1
# 0
# 1
# 10
# Enter the edge  2
# 0
# 2
# 6
# Enter the edge  3
# 0
# 3
# 5
# Enter the edge  4
# 1
# 3
# 15
# Enter the edge  5
# 2
# 3
# 4
# output:
# 2 - 3: 4
# 0 - 3: 5
# 0 - 1: 10
