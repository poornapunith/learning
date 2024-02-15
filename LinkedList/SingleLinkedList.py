
class Node :
    def __init__(self,value) :
        self.value=value
        self.next=None


class LinkedList :
    def __init__(self) :
        self.head=None
        self.tail=None
        self.length=0

    def InsertAtEnd(self,value):
        new_node=Node(value)
        if(self.head==None):
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1


new_Linked_List = LinkedList()
new_Linked_List.InsertAtEnd(10)
new_Linked_List.InsertAtEnd(20)
print(new_Linked_List.length)
print(new_Linked_List.head.value)