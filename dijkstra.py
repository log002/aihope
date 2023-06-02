def djistra(graph,src):
 
    
   total=len(graph)
   
   dist=[1e7 for i in range(total)]
   vis=[False for i in range(total)]
   
   dist[src]=0
   
   for i in range(total):
       u=-1
       
       for x in range(total):
           if vis[x]==False and (u==-1 or dist[x]<dist[u]):
            u=x
           
       if(dist[u]==1e7):
         break
     
       vis[u]=True
       for node,w in graph[u]:
           if (vis[node]==False and dist[u]+w<dist[node]):
               dist[node]=dist[u]+w
    
    
   return dist


    
graph={
    0: [(1, 1)],
    1: [(0, 1), (2, 2), (3, 3)],
    2: [(1, 2), (3, 1), (4, 5)],
    3: [(1, 3), (2, 1), (4, 1)],
    4: [(2, 5), (3, 1)]
}


print(djistra(graph,0))
