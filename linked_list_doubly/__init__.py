## Class of Node containing data and two pointers namely next and prev in DLL

class Node:
    ## initializing the data and nodes of singly linked list

    def __init__(self,data=None ):
        self.data = data
        self.prev = None
        self.next = None

## class of DLL

class Doubly_linked_list:
    ## initializing head node

    def __init__(self):
        self.head = None

## Insertion in the beginning of the DLL
    def insert_at_beginning(self,data):
        node = Node(data)

        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        self.head = node


## Displaying all the elements in list

    def printd(self):
        if self.head is None:
            print("List has no element")
            return
        else:
            iterator = self.head
            while iterator is not None:
                print(iterator.data,end="-->")
                iterator = iterator.next


## Deleting the nodes in DLL

    def deleteNode(self,deleted_node):
        ##checking the null condition for the head and the deleted_node
        if self.head is  None or deleted_node is None:
            return
        ## Deleting the first node
        if self.head == deleted_node:
            self.head = deleted_node.next
        ## if the node to be deleted is not the first node Change the pointer
        if deleted_node.prev is not None:
            deleted_node.prev.next = deleted_node.next
        ##  if the node to be deleted is not the last node Change the next pointer
        if deleted_node.next is not None:
            deleted_node.next.prev = deleted_node.prev
        """## if deleted node is the last node
        if deleted_node.next is None:
            deleted_node.prev.next = deleted_node.next"""



if __name__ == '__main__':
    d = Doubly_linked_list()
    d.insert_at_beginning(2)
    d.insert_at_beginning(4)
    d.insert_at_beginning(5)
    d.insert_at_beginning(10)
    d.insert_at_beginning(12)
    d.printd()
    d.deleteNode(d.head.next.next.next.next)  ## Deleting the secong node in the linked list
    print("\n Doubly Linked List after deletion")
    d.printd()













