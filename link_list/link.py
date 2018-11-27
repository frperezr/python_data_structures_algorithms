class Node(object):

    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0
    # O(1)
    def insertStart(self, data):
        # update size to current size + 1
        self.size = self.size + 1
        # generate a new node
        newNode = Node(data)
        # if there is no head, is the first element of the linkedlist
        if not self.head:
            # asign the head to the new node object
            self.head = newNode
        # else is not the first element
        else:
            # so configure the new node to point to this head
            newNode.nextNode = self.head
            # update the head with the new node (that has the info of the previous node)
            self.head = newNode
            # finaly this is like
            # self.head = {
            #  nextNode = {
            #   nextNode = {
            #    nextNode = {
            #     nextNode = {
            #      null,
            #      data: a
            #     }, data: b
            #    }, data: c
            #   }, data: d
            #  }, data: e
            # data: f
            # }

    def remove(self, data):
        # if there is no elements, return
        if self.head is None:
            return
        # reduce the size by 1
        self.size = self.size - 1
        # set the current node to this head
        currentNode = self.head
        # set a previous node of none
        previousNode = None
        # while the current node data dont match the data we want delete:
        while currentNode.data != data:
            # the previous node will be the current node (we are iterating the list)
            previousNode = currentNode
            # and the current node will be the next node of the list
            currentNode = currentNode.nextNode
        # if the previousNode is none:
        if previousNode is None:
            # this head will be the next node
            self.head = currentNode.nextNode
        else:
            # else the next node of the previousNode will be the next node of the current node
            # that because we are deleting the current node and we need to make a reference in both
            # previous and next node
            previousNode.nextNode = currentNode.nextNode

    # O(1)
    def size1(self):
        return self.size

    # O(N) not good
    def size2(self):
        actualNode = self.head
        size = 0

        while actualNode is not None:
            size += 1
            actualNode = actualNode.nextNode

        return size

    # O(N)
    def insertEnd(self, data):
        # increase size by one
        self.size = self.size + 1
        # make a new node
        newNode = Node(data);
        # reference the actual node with the actual head
        actualNode = self.head;
        # find the end of the linked list
        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode
        # update actual node
        actualNode.nextNode = newNode

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def traverseList(self):
        # iterate throw the list
        actualNode = self.head
        # while the actual node is not pointing none (the last one)
        while actualNode is not None:
            # print the data of the node
            print("%d " % actualNode.data)
            # and set the actual node to the next one to iterate throw it
            actualNode = actualNode.nextNode

linkedlist = LinkedList()

linkedlist.insertStart(12)
linkedlist.insertStart(122)
linkedlist.insertStart(3)
linkedlist.insertEnd(31)

print(linkedlist)

linkedlist.traverseList()

print(linkedlist.size1())

linkedlist.remove(31)
linkedlist.remove(12)
linkedlist.remove(122)
linkedlist.remove(3)

print(linkedlist.size1())
