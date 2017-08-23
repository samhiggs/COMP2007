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
	# print("Path result is ", path[1])
	while queue:
		current = queue.popleft()
		# print(queue)
		adjNodes = graph.get(current)
		# print(current, " has adjacent nodes ", adjNodes)
		if adjNodes is not None:
			# print("current ", current)
			# print("adjacent nodes ",adjNodes)
			# for adjNode in adjNodes:
			for adjNode in adjNodes:
				if adjNode not in visited:
					if adjNode == path[1]:
						return 1
					visited.add(adjNode)
					queue.append(adjNode)
	return 0

# Read in the number of vertices (n) and edges (m)
n = int(input())
m = int(input())

edges, queries = [], []
graph = {}
for _ in range(m):
    edges.append(input().split())

for edge in edges:
	graph

q = int(input())

for _ in range(q):
    queries.append(input().split())
	
# Print a `1` to stdout for each query. This section should be altered to instead print a `1` where the
# query indicates a connection and `0` else.
# for query in queries:
# print (query)
graph = graph_init(edges)
# for key, value in sorted(graph.items()):
# 	print(key,value)
# cntr = 0
for path in queries:
	# print("path ", path)
	result = BFS(graph, path)
	print(result)
# 	if result == 0:
# 		print("There is a path between", path)
# 		cntr += 1
# print(cntr)

#GENERIC CODE#
# for _ in queries:
#    print(int(True))
# for edge in edges:
# 	print(edge)