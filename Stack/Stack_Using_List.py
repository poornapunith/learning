

class Stack:
    def __init__(self):
        self.list=[]

    def __str__(self):
        values=self.list.reverse()
        values=[str(x) for x in self.list]
        return "\n".join(values)
    
    def isEmpty(self):
        if (self.list==[]):
            return True
        else:
            return False
        
    def push(self,value):
        self.list.append(value)

customStack=Stack()
customStack.push(10)
customStack.push(20)
customStack.push(30)
print(customStack)

    