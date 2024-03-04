class Queue:
    def __init__(self) :
        self.list=[]

    def __str__(self) :
        l=[str(x) for x in self.list]
        s=" ".join(l)
        return s
    
    def isEmpty(self):
        if (self.list==[]):
            return True
        else:
            return False
        
    def enqueue(self,value):
        self.list.append(value)
        return "Element inserver at end of Queue"
    
    def dequeue(self):
        if (self.isEmpty()):
            return "Queue is Empty"
        else:
            return (self.list.pop(0))
        
    def peek(self):
        if (self.isEmpty()):
            return "Queue is Empty"
        else:
            return (self.list[0])
        
    def delete(self):
        self.list=[]
    

customQueue = Queue()
print(customQueue.isEmpty())

customQueue.enqueue(10)
customQueue.enqueue(20)
customQueue.enqueue(30)
print(customQueue.isEmpty())
print(customQueue)
print(customQueue.dequeue())
print(customQueue)
print(customQueue.peek())
customQueue.delete()
print(customQueue)