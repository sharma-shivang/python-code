class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtHead(self, data):
        if self.head is None:
            newNode = Node(data)
            self.head = newNode
            self.tail = newNode
            return

        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode   

    def insertAtTail(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return

        self.tail.next = newNode
        self.tail = newNode




    def insertAtPosition(self, data, position):

        if position < 1:
            self.insertAtHead(data)
            return

        #step 1 :- curr or temp 
        curr = self.head
        temp = self.head

        #step 2 :- curr ot temp ko position tak le jana
        cnt = 1
        while cnt < position:
            curr = curr.next
            temp = temp.next
            cnt += 1
        temp = temp.next

        #step3 :- new node create karna
        newNode = Node(data)

        #step 4 :- new node ko position par insert karna
        curr.next = newNode
        newNode.next = temp   




    def insertAfter(self, data, after):

        curr = self.head

        while curr.data != after:
            curr = curr.next
            if curr is None:
                print("Node with data", after, "not found.")
                return 

        temp = curr.next
        newNode = Node(data)
        curr.next = newNode
        newNode.next = temp    





        #delete from head
    def deleteFromHead(self):
        if self.head is None:
            print("List is empty.")
            return
        
        self.head = self.head.next


    #delete from tail
    def deleteFromTail(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head   
        if temp.next is None:
            self.head = None
            self.tail = None
            return 

        while temp.next.next is not self.tail:
            temp = temp.next        

        temp.next = None
        self.tail = temp

        #delete after

    def deleteAfter(self, after):
        curr = self.head

        while curr.data != after:
            curr = curr.next
            if curr is None or curr.next is None:
                print("Node with data", after, "not found or has no next node.")
                return

        temp = curr.next.next
        curr.next = temp        


        #delete before

    def deleteBefore(self, before):
        curr = self.head

        while curr.next.next.data != before:
            curr = curr.next
            if curr is None or curr.next is None:
                print("Node with data", before, "not found or has no previous node.")
                return

        temp = curr.next.next
        curr.next = temp    
        #delete at position(Aapka homework hai ye)



    def displayList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("X")        



#main function 

list1 = LinkedList()
list1.insertAtHead(5)
list1.insertAtHead(4)
list1.insertAtHead(2)
list1.insertAtHead(1)

list1.displayList()  

list1.insertAtPosition(3, 2)
list1.displayList()


list1.insertAfter(6, 3)
list1.displayList()

list1.deleteAfter(3)
list1.displayList()

list1.deleteBefore(5)
list1.displayList()
