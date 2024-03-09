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
