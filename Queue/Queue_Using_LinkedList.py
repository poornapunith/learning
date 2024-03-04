class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class queue:
    def __init__(self) :
        self.head=None
        self.tail=None

    def __str__(self) :
        temp=self.head
        s=""
        while(temp):
            s+=str(temp.value)
            s+="-"
            temp=temp.next
        return s
    
    def isEmpty(self):
        if(self.head==None):
            return True
        else:
            return False

    def enqueue(self,value):
        newNode=Node(value)
        if (self.head==None):
            self.head=self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode

    def dequeue(self):
        if (self.isEmpty()):
            return "Queue is Empty"
        else:
            temp=self.head
            if(self.head==self.tail):
                self.head=self.tail=None
            else:
                self.head=self.head.next
            return temp.value
        
    def peek(self):
        if (self.isEmpty()):
            return "Queue is Empty"
        else:
            return (self.head.value)
        
    def delete(self):
        self.head=self.tail=None



customQueue = queue()
customQueue.enqueue(10)
customQueue.enqueue(20)
customQueue.enqueue(30)
print(customQueue)
print(customQueue.dequeue())
print(customQueue)
print(customQueue.peek())
customQueue.delete()
