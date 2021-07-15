# Defines the node objects

class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.search = False
        self.parent = None

    def addEdge(self, road):
        self.edges.append(road)
        print(self.value, road)
