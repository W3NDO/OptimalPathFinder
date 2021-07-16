class Graph:
    def __init__(self):
        self.nodes = []
        self.graph = {}
        self.start = None
        self.end = None

    def addNode(self, node):
        #Node into array for lookup later
        self.nodes.append(node)
        title = node.value

        #node into dictionary
        self.graph[title] = node

    def getNode(self, node):
        temp = self.graph[node]
        return temp
       
    def setStart(self, town):
        self.start = self.graph[town]
        return self.start

    def setEnd(self, town):
        self.end = self.graph[town]
        return self.end
