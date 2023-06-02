from collections import defaultdict as dd

adj=dd(list)

def graphColoring(adj,vertices):
    
    result=[-1 for i in range(vertices) ]
    
    result[0]=0
    
    available_colors=[False for i in range(vertices) ]
    
    
    for node in range(1,vertices):
        
        
        for adjnode in adj[node]:
            if result[adjnode]!=-1:
                available_colors[result[adjnode]]=True
        
        
        color=0
        
        while color<vertices:
            
            if(available_colors[color]==False):
                break
            
            color=color+1
            
        
        
        result[node]=color
        
        for adjnode in adj[node]:
            if result[adjnode]!=-1:
                available_colors[result[adjnode]]=False
        
    
    print("vertex","----","color_assigned")
    print()
    for node in range(vertices):
        print(node,"----",result[node])
        
  
p=int(input("Enter the no of vertices"))



e=int(input("Enter the no of edges"))

i=0

print("Enter the edges ")

while e>0:
    
    u=int(input())
    v=int(input())
    adj[u].append(v)
    adj[v].append(u)
    
    
    e=e-1
    
graphColoring(adj,p)
    

    
    
