
class Node :
    def __init__(self,value) :
        self.value=value
        self.next=None


class LinkedList :
    def __init__(self) :
        self.head=None
        self.tail=None
        self.length=0

    def __str__(self) :
        temp=self.head
        out=""
        while (temp != None):
            out+= str(temp.value)
            if (temp.next != None):
                out+=" -> "
            temp=temp.next
        return out
    
    def InsertAtBeginning (self,value):
        new_node=Node(value)
        if(self.head==None):
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1

    


new_Linked_List = LinkedList()
new_Linked_List.InsertAtEnd(10)
new_Linked_List.InsertAtEnd(20)
new_Linked_List.InsertAtBeginning(30)
new_Linked_List.InsertAtIndex(0,50)
new_Linked_List.InsertAtIndex(20,150)
print(new_Linked_List)