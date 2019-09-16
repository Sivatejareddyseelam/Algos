class graph:
    def __init__(self):
        self.graph={}

    def __getitem__(self,item):
        return self.graph[item]

    def addedge(self,u,v):
        if u not in self.graph.keys():
            self.graph[u]=[v]
        else:
            self.graph[u].append(v)
    def length(self):
        return len(self.graph)

class stack:
    def __init__(self):
        self.item=[]
    def is_empty(self):
        return self.item==[]
    def push(self,data):
        self.item.append(data)
        return True
    def pop(self):
        if not self.is_empty():
            return self.item.pop()

def dfs(graph,s,visited):
    visited[s]=True
    print(s)
    for i in graph[s]:
        if not visited[i]:
            dfs(graph,i,visited)

g = graph()
g.addedge(0, 1)
g.addedge(0, 2)
g.addedge(1, 2)
g.addedge(2, 0)
g.addedge(2, 1)
g.addedge(2, 3)
g.addedge(3,2)
visited=[False]*g.length()
dfs(g,2,visited)