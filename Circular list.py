class node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class circularlist:
    def __init__(self):
        self.head=node(None)
        self.head.next=self.head
        self.length=0
    def add_node(self,data):
        self.head.next=node(data,self.head.next)
        self.length+=1
