from collections import deque
import heapq

nodeSet = {}
rank = {}

def makeset(node):
    nodeSet[node] = node
    rank[node] = 0

def union(nodeA, nodeB):
    #I Need to find the root of the nodes to unionise.
    rootA = find(nodeA)
    rootB = find(nodeB)
    if(rootA != rootB):
    	if(rank[rootA] <= rank[rootB]):
    		nodeSet[rootA] = rootB
		    if(rank[rootA] == rank[rootB]):
		    	rank[rootB] += 1
    	else:
    		nodeSet[rootB] = rootA



#returns the set that the node belongs to.        
def find(node):
    while nodeSet[node] != node:
        nodeSet[node] = find(nodeSet[node])
    return nodeSet[node]
    
#function to generate a graph
def graph_init(data):
	graph = {}
	for edges in data:
		if edges[0] in graph:
			graph.get(edges[0]).append(edges[1])
		else:
			graph[edges[0]] = [edges[1]]
		if edges[1] in graph:
			graph.get(edges[1]).append(edges[0])
		else: 
			graph[edges[1]] = [edges[0]]
	return graph  

################union find algorithm##################
nodeMap = {}
#makeset initialises every element as it's own set. there will begin with n sets.
def makeset(node):
	nodeMap[node] = node

#union combines 2 elements from different sets
def union(nodeA, nodeB):
	if(nodeMap[nodeA] != nodeA):
		nodeMap[nodeB] = nodeA
	else:
		nodeMap[nodeA] = nodeB
#this looks for the set in which the node is 
def findset(node):
	return nodeMap[node]


#OUTPUT: connected graph, @graph, that uses the minimum weight from the edges in @queue
def Kruskal(graph, queue):
	cost = 0;
	for edge in queue:
		# if both vertices have been visited, then a cycle will be created or the edge already exists
		# so we want to not do anything.
		if(edge[0] in graph  and edge[1] in graph):
			continue
		else:
			#this sneaky devil will add k,v pair only if it doesn't exist.
			graph.setdefault(edge[0], edge[1])
			graph.setdefault(edge[1], edge[0])

			# if(edge[0] in graph):
			# 	graph.get(edge[0]).append(edge[1])
			# else:
			# 	graph[edge[0]] = graph[edge[1]]
			# if(edge[1] in graph):
			# 	graph.get(edge[1]).append(edge[0])
			# else:
			# 	graph[edge[1]] = graph[edge[0]]
			cost += float(edge[2]) #add the weight of the edge.
	print("%.2f" % round(cost,2))
	# print(cost)

# Read in the number of vertices (n) and edges (m)
n = int(input())
m = int(input())

possibleNodes, existingNodes = [], []

graph = {}
queue = []
cost = 0

for _ in range(m):
    possibleNodes.append(input().split())

#a is the number of existing edges.
a = int(input())

for _ in range(a):
    existingNodes.append(input().split())


# print("Possible Edges: ")
# for edge in possibleNodes:
# 	print(edge)
# print("Existing Edges: ")
# for edge in existingNodes:
# 	print(edge)

graph = graph_init(existingNodes)
# for k,v in graph.items():
# 	print(k," ", v)
Kruskal(graph, possibleNodes)
# for node in possibleNodes:
# 	print(node)

# for node in existingNodes:
# 	print(node)
