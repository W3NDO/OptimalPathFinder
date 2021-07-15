class Graph:
    def __init__(self):
        self.nodes = []
        self.graph = {}

    def addNode(self, node):
        #Node into array for lookup later
        self.nodes.append(node)
        title = node.value

        #node into dictionary
        self.graph[title] = node

    def getNode(self, node):
        temp = self.graph[node]
        