class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None
class BST:
    def addNode(self,root,value):#method declaration
        Newnode=Node(value)#method defination
        if root==None:
            return Newnode
        else:
            if value<root.data:
                if root.left==None:
                    root.left=Newnode
                else:
                    self.addNode(root.left,value)
            else:
                if root.right==None:
                    root.right=Newnode
                else:
                    self.addNode(root.right,value)

    def inorder(self,root):
        if root.left!=None:
            self.inorder(root.left)
        print(root.data,end="-->")
        if root.right!=None:
            self.inorder(root.right)
            
    def preorder(self,root):
        print(root.data,end="-->")
        if root.left!=None:
            self.preorder(root.left)
        if root.right!=None:
            self.preorder(root.right)
            
    def postorder(self,root):
        if root.left!=None:
            self.postorder(root.left)
        if root.right!=None:
            self.postorder(root.right)
        print(root.data,end="-->")
        
    def levelorder(self,root):
        q=[root]
        while len(q)!=0:
            ele=q.pop(0)
            print(ele.data,end="-->")
            if ele.left!=None:
                q.append(ele.left)
            if ele.right!=None:
                q.append(ele.right)

values=[16,9,25,4,10,8,83,15]
tree=BST()
root=tree.addNode(None,values[0])
for i in range(1,len(values)):
    tree.addNode(root,values[i])
tree.inorder(root)
print()
tree.preorder(root)
print()
tree.postorder(root)
print()
tree.levelorder(root)