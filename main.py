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
    print(graph.nodes)
