"""Data Structure : Linked List

Implementation : Singly Linked List

Operation Performed:

Insertion of an element
Count of an element in a Linked List
Removal of an element in a Linked List"""



## initializing the data and nodes of singly linked list

class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data  ## storing the element
        self.next_node = next_node   ## storing the address of next element

## initializing head node

class linked_list:
    def __init__(self):
        self.head = None

    ## Displaying all the elements in list

    def printll(self):
        ## checking if elements present in Singly Linked List
        if self.head is None :
            print("Empty Singly Linked List")
            return
        ## now if not null printing all the elements
        iterator = self.head ## taking the head into object
        lst_str = ' '  ## creating the string object
        while iterator:
            lst_str += str(iterator.data) + '-->' ## castyping the data into string
            iterator = iterator.next_node
        print(lst_str)

    ## Insertion of an element
    ## 1. Beginning of the Linked List
    ## Time Complexity : O(1)

    def insert_at_beginning(self,data):
        node = Node(data,self.head)  ## passing the head and the data to Node class so as to copy the address of next node/second node to node that is being inserted
        self.head = node   ## copying the new node to the head node by self.head

    ##  ## 2. End of the Linked List
    ## Time Complexity : O(n)

    def insert_at_end(self,data):
        ## checking for condition whether the linked list is emplty
        if self.head is None:
            self.head = Node(data,None)
            return

        iterator = self.head
        while iterator.next_node:  ## we need to stop at the last second element
            iterator= iterator.next_node  ## iterator will store the last second element address
        iterator.next_node = Node(data,None)  ## in the null node we will store the last element

    ## Method to count number of elements inside Linked List
    def count_length(self):
        count = 0
        iterator = self.head
        while iterator:
            count += 1
            iterator = iterator.next_node
        return count

    ## inserting at any of the index

    def insert_at_index(self, data, idx):
        ## checking if the idx given is not negative or greater than length of list
        if idx < 0 or idx > self.count_length():
            raise Exception("Invalid Index")

        ## Inserting at the first index
        if idx == 0:
            self.insert_at_beginning(data)
            return

        ## inserting elements at other indexes

        count = 0
        iterator = self.head
        while iterator:
            if count == idx - 1 :  ## because count will start from 0 so position user will give should always be less then 1
                node = Node(data,iterator.next_node) ## to insert at 4th we need to first get the address of 4th position
                iterator.next_node = node ## again the

            iterator = iterator.next_node ##if idx-1 not equal the do iterator.next_node
            count += 1

##  Method Definition to reverse the elements inside the linked list

    def reverse_list(self):
        curr = self.head
        next = None
        prev = None

        while curr is not None:
            next = curr.next_node
            curr.next_node = prev
            prev = curr
            curr = next
        self.head = prev



if __name__  ==  '__main__':
  list_1 = linked_list()
  list_1.insert_at_beginning(45)
  list_1.insert_at_beginning(50)
  list_1.printll()
  list_1.insert_at_end(46)
  list_1.insert_at_end(34)
  list_1.printll()
  list_1.insert_at_index(37,2)
  list_1.printll()
  list_1.reverse_list()
  print("Linked List after reversal operation:")
  list_1.printll()





































