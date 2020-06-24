class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printLinkedList(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

    def append(self, newData):
        newNode = Node(newData)

        # First create a check for empty head.
        if self.head is None:
            self.head = newNode
            return

        # Creating a first Node and calling it last node for now.
        last_node = self.head

        while last_node.next is not None:
            # Creating a node.next and linking it to subsequent node.
            last_node = last_node.next

        # Creating a node.next that wil link to the second Node.
        last_node.next = newNode


    def prepend(self, pdata):
        new_Prenode = Node(pdata)
        new_Prenode.next = self.head
        self.head = new_Prenode

    def deleteNode(self, key):
        curr_node = self.head

        # Below code is for deleting the head only
        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return

        prev = None
        while curr_node and curr_node.data != key:
            prev = curr_node
            print("prev is: ", prev.__dict__)
            curr_node = curr_node.next
            print("curr_node is: ", curr_node.__dict__)

        if curr_node is None:
            return


        prev.next = curr_node.next
        curr_node = None


obj = LinkedList()
obj.append("A")
obj.append("B")
obj.append("C")
obj.append("D")
obj.append("E")
obj.append("F")
obj.append("G")
obj.append("H")

obj.deleteNode("E")



obj.printLinkedList()



