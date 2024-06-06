def BFS(key,graph):
            res=[key]
            visited=[key]
            while len(res)>0:
                ele=res.pop(0)
                for i in graph[ele]:
                    if i not in visited:
                            res.append(i)
                            visited.append(i) 
            return visited 
def DFS(start,graph,visited=None):
    if visited==None:
        visited=[]
    visited.append(start)
    for i in graph[start]:
        if i not in visited:
            DFS(i,graph,visited)
    return visited

graph={'A':['B','C'],
   'B':['A','C','D'],
   'C':['A','B','E'],
   'D':['B','E'],
   'E':['C','D']
   }
start=input()
# print(BFS(start,graph))
print(DFS(start,graph))