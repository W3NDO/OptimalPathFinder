import json
import node as node
import graph as graph


#Import the town data
dataFile = open('towns.json')
data = json.load(dataFile)
dataFile.close()

#Create Graph object
graph = graph.Graph()

towns = data["towns"]

for i in range(len(towns)):
    town = towns[i]["name"]
    roads_to = towns[i]["roads_to"]
    n = node.Node(town)
    
    for j in range(len(roads_to)):
        road = roads_to[j]
        n.addEdge(road)
        # print(road)

    graph.addNode(n)
    #print(graph.nodes)

def BreadthFirst(start, end):
    start =graph.setStart(start)
    end = graph.setEnd(end)

    queue = []

    start.searched = True
    queue.append(start)

    while len(queue) > 0:
        current = queue.pop(0)
        #print("Checking: ", current.value)
        if current == end:
            print("Found Target:", current.value)
            break

        edges = current.edges
        for edge in edges:
            neighbour = graph.getNode(list(edge.keys())[0])
            # print("Neighbour: ", neighbour.value)
#           print(current.value, "is neighbours with ", neighbour.value)
            if not neighbour.searched:
                neighbour.searched = True
                neighbour.parent = current
                queue.append(neighbour)

    path = []
    path.append(end)
    nextNode = end.parent
    while nextNode != None:
        path.append(nextNode)
        nextNode = nextNode.parent

    txt = "Path using BFS :: "

    for i in range(len(path))[::-1]:
        n = path[i]
        txt += n.value 
        if i != 0:
            txt += " --> "

    print(txt) 

def DepthFirst(start, end):
    start = graph.setStart(start)
    end = graph.setEnd(end)

    stack = []
    start.searched = True
    stack.append(start)

    while len(stack) > 0:
        current = stack.pop()
        # print("Checking: ", current.value)
        if current == end:
            print("Found : ", current.value)
            break
        edges = current.edges
        for edge in edges:
            neighbour = graph.getNode(list(edge.keys())[0])
            # print("Checking Neighbour: ", neighbour.value)
            if not neighbour.searched:
                neighbour.searched = True
                neighbour.Parent = current
                stack.append(neighbour)

    path = []
    path.append(end)
    nextNode = end.parent
    while nextNode != None:
        path.append(nextNode)
        nextNode = nextNode.parent
    txt = "Path using DFS :: "
    for i in range(len(path))[::-1]:
        n = path[i]
        txt += n.value
        if i != 0:
            txt += " --> "
    print(txt)

def aStar(start, end, h):
    #using straight line distance as a heuristic.
    #list of straight line distances is in the variable straight line distances in towns.json
    straight_line_distances = data["straight_line_distances"]
    print(straight_line_distances["Kisumu_Nakuru"])
    print("Path using A* :: ")

BreadthFirst("Kisumu", "Mombasa")
DepthFirst("Kisumu", "Mombasa")
aStar("Kisumu", "Mombasa", 123)




