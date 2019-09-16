class node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    def __str__(self):
        return str(self.data)

n1=node(1)
n2=node(2)
n3=node(3)
n1.next=n2
n2.next=n3
def print_list(n):
    while n is not None:
        print(n)
        n=n.next
    print()
def print_backward(list):
    if list is None:
        return
    head=list
    tail=list.next
    print_backward(tail)
    print(head)
def remove_second(n):
    first=n
    second=n.next
    first.next=second.next
    second.next=None
    return second
class linkedlist:
    def __init__(self):
        self.length=0
        self.head=None
    def addfirst(self,data):
        first=node(data)
        self.head=first
        first.next=None
        self.length+=1
print_list(n1)
print_backward(n1)