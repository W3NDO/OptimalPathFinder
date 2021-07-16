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
# print(towns)
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

start =graph.setStart("Mombasa")
end = graph.setEnd("Kisumu")

queue = []

start.searched = True
queue.append(start)

while len(queue) > 0:
    current = queue.pop(0)
    #print("Checking : ", current.value)
    if current == end:
        print("Found:", current.value)
        break

    edges = current.edges
    for edge in edges:
        neighbour = graph.getNode(list(edge.keys())[0])
#        print(current.value, "is neighbours with ", neighbour.value)
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

txt = "Path :: "

for i in range(len(path))[::-1]:
    n = path[i]
    txt += n.value 
    if i != 0:
        txt += " --> "

print(txt) 
