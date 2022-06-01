class Node:
    
    def __init__(self, data = None, next = None) : 
        
        self.data = data
        self.next = next 
        

class LinkedList :
    
    def __init__(self) :
        
        self.head = None
    
    def insert_at_begining(self, data) :
        node = Node(data, self.head)
        self.head = node 
    
    def print(self) :
        
        if self.head is None:
            print("Empty LinkedList!!!")
            return 
        
        itr = self.head 
        llist = ''
        while itr :
            llist += str(itr.data) + " --> "
            itr = itr.next 
        print(llist + " null")
        
    def insert_at_end(self, data):
        
        if self.head is None:
            self.head = Node(data, None)
            return 
        
        itr = self.head 
        while itr.next:
            itr = itr.next 
        
        itr.next = Node(data, None)
    
    def insert_values_of_list(self, datalist):
        
        for data in datalist:
            self.insert_at_end(data)
    
    def length(self):
        
        count = 0 
        
        itr = self.head
        
        while itr:
            
            count += 1 
            itr = itr.next 
        
        return count
    
    def remove_at(self, index):
        
        if index < 0 or index > self.length():
            raise Exception("Invalid Index")
        
        if index == 0:
         
            self.head = self.head.next
            return 
        
        count = 0 
        
        itr = self.head 
        
        while itr:
            
            if count == index - 1 :
                itr.next = itr.next.next
                break
            
            itr = itr.next 
            count += 1
    
    def insert_at(self, index, data):
        
        if index < 0 or index > self.length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.insert_at_begining(data)
            return
    
        count = 0 
        itr = self.head 
        
        while itr:
            if count == index - 1 :
                node = Node(data, itr.next)
                itr.next = node
                break 
            itr = itr.next 
            count += 1
    
    def print_at(self, index):
        
        if index < 0 or index > self.length():
            raise Exception("Invalid index!!!")
        
        if index == 0 :
            print(self.head.data)
            return 
        
        count =  0 
        itr = self.head 
        
        while itr:
            if count == index :
                print(itr.data)
                break
            itr = itr.next 
            count += 1 

    def insert_after(self, data_after, data_to_insert):
        
        if self.head is None:
            return 
        
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return
        
        itr = self.head 
        
        while itr :
            
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next
    
    
    def remove_after(self, data_after):
        
        if self.head is None:
            return 
        
        if self.head.data == data_after:
            self.head = self.head.next
            return 
        
     
        itr = self.head 
        
        while itr :
            if itr.data == data_after:
                itr.next = itr.next.next
                break
            
            itr = itr.next 
            
ll = LinkedList()
# ll.insert_at_begining(8)
# ll.insert_at_begining(9)
# ll.insert_at_end(20)
# ll.insert_at_end(30)
ll.insert_values_of_list(['a','b','c','d'])
ll.print()
# print("Length of the linkedlist is : {}".format(ll.length()))
# ll.remove_at(3)
# ll.print()
# print("Length of the linkedlist is : {}".format(ll.length()))
# ll.insert_at(3, "f")
# ll.print_at(3)
# ll.insert_after("c","x")
# ll.print()
ll.remove_after("a")
ll.print()