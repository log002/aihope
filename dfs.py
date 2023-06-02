def dfs(graph,vis,v):
    vis[v]=True
    
    print(v,end=" ")
    
    for adjnode in graph[v]:
        if vis[adjnode]==False:
            dfs(graph,vis,adjnode)
            
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

dfs(graph,vis,0)
