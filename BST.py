class Node(object):
    def __init__(self,val,left=None,right=None,parent=None):
        self.val=val
        self.left_child=left
        self.right_child=right
        self.parent=parent
    def get(self):
        return self.val
    def get_left_child(self):
        return self.left_child
    def get_right_child(self):
        return self.right_child
class Search_Tree(object):
    def __init__(self,root=None):
        self.root=root
        self.size=0
    def search(self,root,val):
        if not self.root:
            return False
        elif self.root.val==val:
            return True
        else:
            if val<self.root.val:
                self.search(self.root.left_child,val)
            else:
                self.search(self.root.right_child,val)

    def insert(self,root,val):
        if root.val==None:
            self.root=val
        if val< root.val:
            if root.left_child:
                self.insert(root.left_child,val)
            else:
                root.left_child=Node(val)
                root.left_child.parent=root
        else:
            if root.right_child:
                self.insert(root.right_child,val)
            else:
                root.right_child=Node(val)
                root.right_child.parent=root
    