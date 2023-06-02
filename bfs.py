def bfs(graph,vis):
    queue=[]
    
    vis[0]=True
    
    queue.append(0)
    
    while queue:
        node=queue.pop(0)
        print(node,end=" ")
        
        for adjnode in graph[node]:
            if vis[adjnode]==0:
                queue.append(adjnode)
                vis[adjnode]=1

graph={
    0:[1,2],
    1:[0,3],
    2:[0,3],
    3:[1,2]
}

v=4

vis=[]

for i in range(4):
    vis.append(False)

bfs(graph,vis)
