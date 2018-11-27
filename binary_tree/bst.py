class Node(object):

    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def insert(self, data):
        # the first item of the binary search tree
        if not self.root:
            # set the root to be a new Node
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)

    def insertNode(self, data, node):
        # check if the node data is greater than the data we want to store
        if data < node.data:
            # check if the node have a left child
            if node.leftChild:
                # the node have a left child, run the func again to check the next node
                self.insertNode(data, node.leftChild)
            # the node dont have a left child
            else:
                # make a new node and asign it to the left child
                node.leftChild = Node(data)
        else:
            # if there is a right child, check if the next node have one
            if node.rightChild:
                self.insertNode(data, node.rightChild)
            else:
                # if there is no right child, make a new one
                node.rightChild = Node(data)

    def removeNode(self, data, node):
        if not node:
            return node
        if data < node.data:
            node.leftChild = self.removeNode(data, node.leftChild)
        elif data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild)
        else:
            # this is a leaf node
            if not node.leftChild and not node.rightChild:
                print("Removing a leaf node...")
                del node
                return None
            # one leaf
            if not node.leftChild:
                print("Removing a node with a single right child...")
                tempNode = node.rightChild
                del node
                return tempNode
            elif not node.rightChild:
                print("Removing a node with a single left child...")
                tempNode = node.leftChild
                del node
                return tempNode
            # two leafes
            print("Removing node with two children...")
            # find predeccor
            tempNode = self.getPredecessor(node.leftChild)
            # swap with the root
            node.data = tempNode.data
            # delete the item
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)

        return node

    def getPredecessor(self, node):
        if node.rightChild:
            return self.getPredecessor(node.rightChild)
        return node

    def remove(self, data):
        # if root is not None => data exists
        if self.root:
            # set the root to be the reference of the deleted node
            self.root = self.removeNode(data, self.root)

    def getMinValue(self):
        # if the root is not none => there are items
        if self.root:
            return self.getMin(self.root)

    def getMin(self, node):
        # a left child exists
        if node.leftChild:
            # go to the next left child
            return self.getMin(node.leftChild)
        # we are on last leaf of the tree, so just return the min value of the tree
        return node.data

    def getMaxValue(self):
        # if the root is not None, data exists
        if self.root:
            # return the max value
            return self.getMax(self.root)

    def getMax(self, node):
        # check if the node have a right child
        if node.rightChild:
            # if it have one, repeat the operation to get the next one
            return self.getMax(node.rightChild)
        # we are on the last leaf of the tree, so just return the max value of the tree
        return node.data

    def traverse(self):
        # if the root is not None
        if self.root:
            self.traverseInOrder(self.root)

    def traverseInOrder(self, node):
        # check if left child exists (is not None)
        if node.leftChild:
            # run the function again with the next leftChild
            self.traverseInOrder(node.leftChild)
        # print root node => not the main root node
        print("%s " % node.data)
        # check if the right child exists (is not None)
        if node.rightChild:
            # run the function again with the next rightChild
            self.traverseInOrder(node.rightChild)

bst = BinarySearchTree()
bst.insert(10)
bst.insert(13)
bst.insert(5)
bst.insert(14)

bst.remove(10)
# print(bst.getMinValue())
# print(bst.getMaxValue())
bst.traverse()
