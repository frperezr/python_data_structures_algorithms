
class Node(object):

    def __init__(self, data):
        self.data = data;
        self.height = 0;
        self.leftChild = None;
        self.rightChild = None;

class AVL(object):

    def __init__(self):
        self.root = None;

    def insert(self, data):
        self.root = self.insertNode(data, self.root);

    def insertNode(self, data, node):
        # check if is not the first element (the root)
        if not node:
            return Node(data);

        if data < node.data:
            node.leftChild = self.insertNode(data, node.leftChild);
        else:
            node.rightChild = self.insertNode(data, node.rightChild);

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1;

        return self.settleViolation(data, node);

    def settleViolation(self, data, node):

        balance = self.calcBalance(node);

        # case 1 -> left left heavy situation
        if balance > 1 and data < node.leftChild.data:
            print("Left left heavy situation...");
            return self.rotateRight(node);
        # case 2 -> right right heavy situation
        if balance < -1 and data > node.rightChild.data:
            print("Right right heavy situation...");
            return self.rotateLeft(node);
        # case 3 -> left right heavy situation
        if balance > 1 and data > node.leftChild.data:
            print("Left right heavy situation...");
            node.leftChild = self.rotateLeft(node.leftChild);
            return self.rotateRight(node);
        # case 4 -> right left heavy situation
        if balance < -1 and data < node.rightChild.data:
            print("Right left heavy situation");
            node.rightChild = self.rotateRight(node.rightChild);
            return self.rotateLeft(node);

        return node;

    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root);

    def removeNode(self, data, node):

        if not node:
            return node;

        if data < node.data:
            node.leftChild = self.removeNode(data, node.leftChild);
        elif data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild);
        else:

            if not node.leftChild and not node.rightChild:
                print("Removing a leaf node...");
                del node;
                return None;
            if not node.leftChild:
                print("Removing a node with a right child...");
                tempNode = node.rightChild;
                del node;
                return tempNode;
            elif not node.rightChild:
                print("Removing a node with a left child...");
                tempNode = node.leftChild;
                del node;
                return tempNode;

            print("Removing node with two children");
            tempNode = self.getPredecessor(node.leftChild);
            node.data = tempNode.data;
            node.leftChild = self.removeNode(tempNode.data, node.leftChild);

        if not node:
            return node; # if the tree had just a single node

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1;

        balance = self.calcBalance(node);

        # doubly left heavy situation
        if balance > 1 and self.calcBalance(node.leftChild) >= 0:
            return self.rotateRight(node);
        # left right case
        if balance > 1 and self.calcBalance(node.leftChild) < 0:
            node.leftChild = self.rotateLeft(node.leftChild);
            return self.rotateRight(node);
        # doubly right case
        if balance < -1 and self.calcBalance(node.rightChild) <= 0:
            return self.rotateLeft(node);
        # right left case
        if balance < -1 and self.calcBalance(node.rightChild) > 0:
            node.rightChild = self.rotateRight(node.rightChild);
            return self.rotateLeft(node);

        return node;

    def getPredecessor(self, node):
        if node.rightChild:
            return self.getPredecessor(node.rightChild);

        return node;

    def calcHeight(self, node):
        # if is a null pointer return -1
        if not node:
            return -1;

        return node.height;

    # if it return value > 1 it means is a left heavy tree --> right rotation
    # if it return value < -1 it means it is a right heavy tree --> left rotation
    def calcBalance(self, node):
        # if is a leaf node, return 0
        if not node:
            return 0;

        return self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild);

    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root);

    def traverseInOrder(self, node):

        if node.leftChild:
            self.traverseInOrder(node.leftChild);
        print("%s " % node.data);
        if node.rightChild:
            self.traverseInOrder(node.rightChild);

    def rotateRight(self, node):
        print("rotating to the right on node ", node.data);
        # get the left child of the root
        tempLeftChild = node.leftChild;
        # get the right child of the tempLeftChild
        t = tempLeftChild.rightChild;
        # set the tempLeftChild (the left child of the root) to be the new root
        tempLeftChild.rightChild = node;
        # set the right child of the tempLeftChild to be the leftChild of the prev root
        node.leftChild = t;
        # update the node height
        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1;
        tempLeftChild.height = max(self.calcHeight(tempLeftChild.leftChild), self.calcHeight(tempLeftChild.rightChild)) + 1;

        return tempLeftChild;

    def rotateLeft(self, node):
        print("rotating to the left on node ", node.data);
        # get the left child of the root
        tempRightChild = node.rightChild;
        # get the left child of the tempRightChild
        t = tempRightChild.leftChild;
        # set the tempRightChild (the right child of the root) to be the new root
        tempRightChild.leftChild = node;
        # set the left child of the tempRightChild to be the rightChild of the prev root
        node.rightChild = t;
        # update the node height
        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1;
        tempRightChild.height = max(self.calcHeight(tempRightChild.leftChild), self.calcHeight(tempRightChild.rightChild)) + 1;

        return tempRightChild;

# Tests
avl = AVL();
avl.insert(10);
avl.insert(20);
avl.insert(5);
avl.insert(6);
avl.insert(15);

avl.remove(15);
avl.remove(20);

avl.traverse();
