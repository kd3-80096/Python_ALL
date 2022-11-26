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


if __name__ == '__main__':
    d = Doubly_linked_list()
    d.insert_at_beginning(2)
    d.insert_at_beginning(4)
    d.insert_at_beginning(5)
    d.insert_at_beginning(10)
    d.insert_at_beginning(12)
    d.printd()












