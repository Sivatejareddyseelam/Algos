class node(object):
    def __init__(self,val):
        self.val=val
class edge(object):
    def __init__(self,from_node=None,to_node=None,weight=None):
        self.val=weight
        self.from_node=from_node
        self.to_node=to_node
class graph(object):
    def __init__(self):
        self.graph={}
    def add_edge(self,edge1):
        if edge1.from_node and edge1.to_node in self.graph.keys():
            self.graph[edge1.from_node].append(edge1)
            self.graph[edge1.to_node].append(edge1)
        elif edge1.to_node not in self.graph.keys() and edge1.from_node in self.graph.keys():
            self.graph[edge1.to_node]=[edge1]
            self.graph[edge1.from_node].append(edge1)
        elif edge1.from_node not in self.graph.keys() and edge1.to_node in self.graph.keys():
            self.graph[edge1.from_node]=[edge1]
            self.graph[edge1.to_node].append(edge1)
        else:
            self.graph[edge1.from_node] = [edge1]
            self.graph[edge1.to_node] = [edge1]
    def __getitem__(self, item):
        return self.graph[item]
    def get_vertices(self):
        v=[]
        for i in self.graph.keys():
            v.append(i.val)
        return v
    def get_edges(self):
        ed=[]
        for i in self.graph.keys():
            for j in self.graph[i]:
                if j not in ed:
                    ed.append(j)
        return ed
g=graph()
node1=node("a")
node2=node("b")
node3=node("c")
node4=node("d")
e1=edge(node1,node2,1)
e2=edge(node2,node4,2)
e3=edge(node4,node3,5)
e4=edge(node1,node3,4)
e5=edge(node1,node4,3)
g.add_edge(e1)
g.add_edge(e2)
g.add_edge(e3)
g.add_edge(e4)
g.add_edge(e5)
class Node(object):
    def __init__(self,key,data):
        self.key=key
        self.data=data
class heap(object):
    def __init__(self):
        self.heap=[]
        self.size=0
    def bubble_up(self,i):
        while i>0:
            if self.heap[i//2].key>self.heap[i].key:
                self.heap[i//2],self.heap[i]=self.heap[i],self.heap[i//2]
            i=i//2
    def bubble_down(self,i):
        while 2*i<self.size:
            if 2*i+1<self.size and self.heap[2*i].key>self.heap[2*i+1].key:
                mc_ind=2*i+1
            else:
                mc_ind=2*i
            if self.heap[i].key>self.heap[mc_ind].key:
                self.heap[i],self.heap[mc_ind]=self.heap[mc_ind],self.heap[i]
            i=mc_ind
    def insert(self,k):
        self.heap.append(k)
        self.size=self.size+1
        self.bubble_up(self.size-1)
    def min(self):
        data=self.heap[0]
        self.heap[0]=self.heap[self.size-1]
        self.size-=1
        self.heap.pop()
        self.bubble_down(self,0)
        return data
def MST(g1,source):
    v=set(g.get_vertices())
    x= set(source.val)
    h=heap()
    for edges in g1[source]:
        h.insert(Node(edges.val,edges.to_node))
    T=[source.val]
    mc=0
    print(g.get_edges())
    while x != v:
        l=[]
        for edges in g.get_edges():
            if edges.from_node.val in x and edges.to_node.val not in x:
                l.append(edges)
        w=[]
        for i in l:
            w.append(i.val)
        mc=mc+min(w)
        min_index=w.index(min(w))
        ed=l[min_index]
        x.add(ed.to_node.val)
        print(x)
        T.append(ed.to_node.val)
    return mc,T
