import json
import node as node
import graph as Graph
import aStarNode as A_S_Node
import priorityQueue as P_Queue

import pygame
from pygame.locals import *

#GUI constants
display_width = 800
display_height = 600

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0, 255, 0)
BLUE = (0,0, 255)
GREY = (40,40,40)

#Town display locations
def townDisplay(town, checking):
    color = GREEN
    if checking == True:
        color = RED

    #switch town
    #create switch statement


#Import the town data
dataFile = open('towns.json')
data = json.load(dataFile)
dataFile.close()

towns = data["towns"]
straight_line_distances = data["straight_line_distances"]

def getSLD(target, goal): #function to read the straight line distance.
    keys = []
    index = None
    for elem in straight_line_distances:
        keys.append(elem)

    for key in keys:
        if target in key and goal in key:
            index = key

    return straight_line_distances[index]

def create_graph(graph):
    for i in range(len(towns)):
        town = towns[i]["name"]
        roads_to = towns[i]["roads_to"]
        n = node.Node(town)
        
        for j in range(len(roads_to)):
            road = roads_to[j]
            n.addEdge(road)
            # print(road)

        graph.addNode(n)
        # print(graph.nodes)

steps = []
def step(current):
    steps.append(current)
    return current
    

def create_a_star_graph(graph):
    for i in range(len(towns)):
        town = towns[i]["name"]
        roads_to = towns[i]["roads_to"]
        n = A_S_Node.Node(town)
        
        for j in range(len(roads_to)):
            road = roads_to[j]
            n.addEdge(road)
            # print(road)

        graph.addNode(n)

def BreadthFirst(start, end):
    #Create Graph object
    graph_bfs = Graph.Graph()
    #Add nodes to graph
    create_graph(graph_bfs)

    screen = pygame.display.set_mode((display_width, display_height))
    pygame.init()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(GREY)
        #

    if start not in graph_bfs.nodeNames or end not in graph_bfs.nodeNames:
        print("Unknown Town")
        return 0
    start =graph_bfs.setStart(start)
    end = graph_bfs.setEnd(end)

    queue = []

    start.searched = True
    queue.append(start)

    while len(queue) > 0:
        current = queue.pop(0)
        step(current.value)
        if current == end:
            # print("Found Target:", current.value)
            break

        step(current.value )
        edges = current.edges
        for edge in edges:
            neighbour = graph_bfs.getNode(list(edge.keys())[0])

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
    graph_dfs = Graph.Graph()
    create_graph(graph_dfs)
    
    if start not in graph_dfs.nodeNames or end not in graph_dfs.nodeNames:
        print("Unknown Town")
        return 0
    start = graph_dfs.setStart(start)
    end = graph_dfs.setEnd(end)

    stack = []
    start.searched = True
    stack.append(start)

    while len(stack) > 0:
        current = stack.pop()
        # print("Checking: ", current.value)
        if current == end:
            # print("Found Tagret: ", current.value)
            break
        edges = current.edges
        for edge in edges:
            neighbour = graph_dfs.getNode(list(edge.keys())[0])
            # print("Neighbour: ", neighbour.value)
            if not neighbour.searched:
                neighbour.searched = True
                neighbour.parent = current
                stack.append(neighbour)
                # for i in stack:
                #     print(i.value)

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

def aStar(start, end):
    #using straight line distance (Euclidean Distance) as a heuristic.
    #list of straight line distances is in the variable straight line distances in towns.json
    
    graph = Graph.Graph()
    create_a_star_graph(graph)

    if start not in graph.nodeNames or end not in graph.nodeNames:
        print("Unknown Town")
        return 0

    start = graph.setStart(start)
    end = graph.setEnd(end)

    #We get the straight line distances of all nodes in the graph to the goal node
    #This is the h() value
    #The g() value is the distance from the current node to one if it's neighbours
    #note that f() = g() + h()

    #the lower the f value, the higher up on the priority queue. It will be removed first
    open_list = P_Queue.PriorityQueue() 
    start.setG(0)
    start.setH(getSLD(start.value, end.value))
    start.searched = True
    open_list.addElem((start.setF(start.g + start.h), start)) #at the beginning, the g value is 0. 
    closed_list = []

    while len(open_list.queue) != 0:
        closed_list.append(open_list.queue[0][1].value)
        # print(open_list.queue[0][1].value , {"f: ": open_list.queue[0][1].f , "g: ": open_list.queue[0][1].g, "h: ": open_list.queue[0][1].h} )
        current = open_list.pop()[1]
        if current.value == end.value:
            # print("Found Target:", current.value)
            break

        edges = current.edges
        for edge in edges:
            neighbour = graph.getNode(list(edge.keys())[0])
            if not neighbour.searched:
                neighbour.searched = True
                neighbour.parent = current
                h = getSLD(neighbour.value, end.value )
                g = neighbour.setCummulativeG(current.getEdgeDistance(neighbour.value))
                f = h+g
                neighbour.setF(f)
                neighbour.setG(g)
                neighbour.setH(h)
                
                neighbour.current = current.value
                open_list.addElem((neighbour.f ,neighbour))
                # print(open_list.queue)

    print("Path using AStar :: " ," --> ".join(closed_list))

def run (start, goal):
    BreadthFirst(start, goal)
    DepthFirst(start, goal)
    aStar(start, goal)

run("Kisumu", "Thika")
