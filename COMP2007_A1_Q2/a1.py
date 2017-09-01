from collections import deque
import heapq
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

#OUTPUT: connected graph, @graph, that uses the minimum weight from the edges in @queue
def Kruskal(graph, queue):
	for item in queue:
		if(item[0] in graph  && item[1] in graph):
			continue
		if()
	#for each element in queue
		#if both nodes have been visited 
			#continue



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

for node in possibleNodes:
	print(node)

for node in existingNodes:
	print(node)
