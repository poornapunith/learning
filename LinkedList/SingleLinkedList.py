
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
    
    def traverse(self):
        temp=self.head
        while(temp!=None):
            print(temp.value)
            temp=temp.next

    def search(self,target):
        temp=self.head
        index=0
        while(temp!=None):
            if (temp.value==target):
                return index
            temp=temp.next
            index+=1
        return -1

    
    def InsertAtBeginning (self,value):
        new_node=Node(value)
        if(self.head==None):
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1

    def InsertAtEnd(self,value):
        new_node=Node(value)
        if(self.head == None):
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
    
    def InsertAtIndex (self,index, value):
        new_node=Node(value)
        if (self.head==None):
            self.head=new_node
            self.tail=new_node
        elif (index<0 or index>self.length):
            return False
        elif (index==0):
            new_node.next=self.head
            self.head=new_node
        else:
            temp=self.head
            for i in range(index-1):
                temp=temp.next
            new_node.next=temp.next
            temp.next=new_node
        self.length+=1

    def pop_first(self):
        if(self.length==0):
            return None
        first_node=self.head
        if (self.length==1):
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            first_node.next=None
            return first_node


new_Linked_List = LinkedList()
new_Linked_List.InsertAtEnd(10)
new_Linked_List.InsertAtEnd(20)
new_Linked_List.InsertAtBeginning(30)
new_Linked_List.InsertAtIndex(0,50)
new_Linked_List.InsertAtIndex(20,150)
print(new_Linked_List)
print(new_Linked_List.pop_first().value)
print(new_Linked_List)