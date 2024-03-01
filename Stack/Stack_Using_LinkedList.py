
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Stack:
    def __init__(self):
        self.head=None

    def __str__(self) :
        s=""
        temp=self.head
        while (temp!=None):
            s+=str(temp.value)
            if(temp.next!=None):
                s+="\n"
            temp=temp.next
        return s

    def push(self,value):
        newNode=Node(value)
        newNode.next=self.head
        self.head=newNode

    def pop(self):
        if(self.head==None):
            return "Stack is Empty"
        else:
            element=self.head.value
            self.head=self.head.next
            return element
        
    def peek(self):
        if(self.head==None):
            return "Stack is empty"
        else:
            return self.head.value
        
    def delete(self):
        self.head=None

customStack=Stack()
customStack.push(10)
customStack.push(20)
customStack.push(30)
print(customStack)
print("----------------------")
print(customStack.pop())
print("----------------------")
print(customStack)
print("----------------------")
print(customStack.delete())
print("----------------------")
print(customStack)

