from collections import deque

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

#BFS is a function to search for the existance of a path
#@return true if a path exists, false if not path exists  
#@visited is a set of nodes that have been explored
#@queue is a list. We will only use append and pop which are both O(1) complexity
	#representing a FIFO abstract data structure for adjacent nodes to be stored.
#@graph is represented by an Adjacency List.
#@path is a 2 element tuple. It is important that it is a tuple as it is immutable. 
def BFS(graph, path):
	visited, queue = set(), deque([path[0]])
	queue.append(path[0])
	while queue:
		current = queue.popleft()
		adjNodes = graph.get(current)
		if adjNodes is not None:
			for adjNode in adjNodes:
				if adjNode not in visited:
					if adjNode == path[1]:
						return 1
					visited.add(adjNode)
					queue.append(adjNode)
	return 0

#read_input is a function that takes an input file from argument and parses them into an array of tuples 
#A tuple represents an edge in the format (<start>, <end>, <weight>) 
# Read in the number of vertices (n) and edges (m)
#edges and queries represent lists of tuples
# Read in the number of vertices (n) and edges (m)
n = int(input())
m = int(input())
#edges and queries represent lists of tuples.
edges, queries = [], []
#initialise an empty dictionary
graph = {}

for _ in range(m):
    edges.append(input().split())

for edge in edges:
	graph

q = int(input())

for _ in range(q):
    queries.append(input().split())
#generate graph
graph = graph_init(edges)
#run search on each path.
for path in queries: 
	print(BFS(graph, path))
