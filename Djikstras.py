class graph(object):
    def __init__(self):
        self.nodes=set()
        self.edges={}
    def add_edge(self,from_node,to_node,weight):
        if from_node in self.edges.keys():
            self.edges[from_node].append([to_node,weight])
        else:
            self.edges[from_node]=[[to_node,weight]]
class heap(object):
    def __init__(self):
        self.heap=[]
        self.size=0
    def bubble_up(self,i):
        while i//2>0:
            if self.heap[i]<self.heap[i//2]:
                a=self.heap[i//2]
                self.heap[i//2]=self.heap[i]
                self.heap[i]=a
            i=i//2
    def insert(self,k):
        self.heap.append(k)
        self.size+=1
        self.bubble_up(self.size-1)
    def bubble_down(self,i):
        while i*2 < self.size:
            if self.heap[2*i]<self.heap[2*i+1]:
                mc_ind=2*i
            else:
                mc_ind=2*i+1
            if self.heap[mc_ind]<self.heap[i]:
                a=self.heap[i]
                self.heap[i]=self.heap[mc_ind]
                self.heap[mc_ind]=a
            i=mc_ind
    def min(self):
        data=self.heap[0]
        self.heap[0]=self.heap[self.size-1]
        self.size-=1
        self.heap.pop()
        self.bubble_down(1)
        return data


def djikstras(graph,source):
    visited=set()
    A={source:0}
    path= [source]
    node=source

    while node not in visited:
        visited.add(node)
        min_node=None
        min_edge=0
        if node not in graph.edges.keys():
            break
        else:
            for i in graph.edges[node]:
                if min_edge==0:
                    min_node=i[0]
                    min_edge=i[1]
                elif i[1]<min_edge:
                    min_node=i[0]
                    min_edge=i[1]
        A[min_node]=A[node]+min_edge
        path.append(min_node)
        node=min_node
    return path,A
g=graph()
g.add_edge("s","v",1)
g.add_edge("s","w",4)
g.add_edge("v","w",2)
g.add_edge("v","t",6)
g.add_edge("w","t",3)
print(djikstras(g,"s"))