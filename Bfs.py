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


class queue:
    def __init__(self,max_size):
        self.items=[]
        self.head=0
        self.tail=0
        self.max_size=max_size

    def is_empty(self):
        if self.head==self.max_size-1 or self.tail==0:
            return True
        return False

    def is_full(self):
        if self.tail==self.max_size-1:
            return True
        return False

    def enqueue(self,data):
        if self.is_full():
            return False
        else:
            self.items.append(data)
            self.tail+=1
            return True
    def dequeue(self):
        if self.is_empty():
            return False
        else:
            data=self.items[self.head]
            self.head+=1
            self.tail-=1
            return data

def BFS(graph,s):
    visited=[]
    dic={}
    visited.append(s)
    dic[s]=0
    q=queue(graph.length())
    q.enqueue(s)
    while not q.is_empty():
        f=q.dequeue()
        for i in graph[f]:
            if i not in visited:
                q.enqueue(i)
                visited.append(i)
                dic[i]=dic[f]+1
    return dic
g = graph()
g.addedge(0, 1)
g.addedge(0, 2)
g.addedge(1, 2)
g.addedge(2, 0)
g.addedge(2, 1)
g.addedge(2, 3)
print(BFS(g,2))