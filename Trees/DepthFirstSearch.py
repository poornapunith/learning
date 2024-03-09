class node:
    def __init__(self,value) :
        self.value=value
        self.left=None
        self.right=None

newBT=node("Drinks")
leftchild=node("Hot")
rightchild=node("Cold")
newBT.left=leftchild
newBT.right=rightchild


def preOrder(root):
    if(root==None):
        return
    else:
        print(root.value)
        preOrder(root.left)
        preOrder(root.right)

#preOrder(newBT)
        
def InOrder(root):
    if(root==None):
        return
    else:
        InOrder(root.left)
        print(root.value)
        InOrder(root.right)

#InOrder(newBT)
        
def PostOrder(root):
    if (root==None):
        return
    else:
        PostOrder(root.left)
        PostOrder(root.right)
        print(root.value)

PostOrder(newBT)