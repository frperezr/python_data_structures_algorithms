# Depth First Search
class Node(object):

    def __init__(self, data):
        self.data = data;
        self.adjacencyList = [];
        self.visited = False;
        self.predecessor = None;

class DepthFirstSearch(object):

    def dfs(self, node):

        node.visited = True;
        print("%s " % node.data);

        for n in node.adjacencyList:
            if not n.visited:
                self.dfs(n);

# Test

node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")

node1.adjacencyList.append(node2)
node1.adjacencyList.append(node3)
node2.adjacencyList.append(node4)
node4.adjacencyList.append(node5)

dfs = DepthFirstSearch()
dfs.dfs(node1)
