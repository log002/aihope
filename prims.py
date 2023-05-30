INF = 9999999
# number of vertices in graph
N = 5
v=int(input(" Enter the vertices "))
#creating graph by adjacency matrix method
G = [[0]*v for i in range(v)]


e=int(input(" Enter the edges "))

print()
print("Enter the edges")

i=1
while e>0:
    print("Enter the edge ",i)
    u=int(input())
    v=int(input())
    w=int(input())
    
    G[u][v]=w
    G[v][u]=w
    
    e=e-1
    i=i+1
    
    


selected_node = [0, 0, 0, 0, 0]

no_edge = 0

selected_node[0] = True

# printing for edge and weight
print("Edge : Weight\n")
while (no_edge < N - 1):
    
    minimum = INF
    a = 0
    b = 0
    for m in range(N):
        if selected_node[m]:
            for n in range(N):
                if ((not selected_node[n]) and G[m][n]):  
                    # not in selected and there is an edge
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n
    print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
    selected_node[b] = True
    no_edge += 1


# sample input
# Enter the vertices 9
#  Enter the edges 14

# Enter the edges
# Enter the edge  1
# 0
# 1
# 4
# Enter the edge  2
# 0
# 7
# 8
# Enter the edge  3
# 1
# 2
# 8
# Enter the edge  4
# 1
# 7
# 11
# Enter the edge  5
# 7
# 8
# 7
# Enter the edge  6
# 7
# 6
# 1
# Enter the edge  7
# 2
# 8
# 2
# Enter the edge  8
# 2
# 3
# 7
# Enter the edge  9
# 2
# 5
# 4
# Enter the edge  10
# 6
# 8
# 6
# Enter the edge  11
# 6
# 5
# 2
# Enter the edge  12
# 5
# 4
# 10
# Enter the edge  13
# 5
# 3
# 14
# Enter the edge  14
# 3
# 4
# 9
# Edge : Weight

# output
# 0-1:4
# 1-2:8
# 2-3:7
# 3-4:9
