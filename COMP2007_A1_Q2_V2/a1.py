from collections import deque
import heapq
def elem(el):
	return el[2]
def add_to_graph(graph, edge):
	if edge[0] in graph:
		graph.get(edge[0]).append(edge[1])
	else:
		graph[edge[0]] = [edge[1]]
	if edge[1] in graph:
		graph.get(edge[1]).append(edge[0])
	else: 
		graph[edge[1]] = [edge[0]]
#function to generate a graph
def graph_init(edges):
	graph = {}
	for edge in edges:
		#this sneaky devil will add k,v pair only if it doesn't exist...doesn't seem to work.
		# graph.setdefault(edge[0], edge[1])
		# graph.setdefault(edge[1], edge[0])
		add_to_graph(graph, edge)
	return graph  

def Kruskal(graph, queue):
	cost = 0;
	for k,v in graph.items():
		print(k,v)
	for edge in queue:
		#either cycle or path
		if edge[0] in graph and edge[1] in graph:
			#if it is a path
			print("edge {} is either a cycle or path".format(edge))
			if edge[1] in graph.get(edge[0]):
				print("Edge is a path")
				cost = cost + float(edge[2]) #add the weight of the edge.
			else:
				continue
		#not a cycle or a path
		else:
			add_to_graph(graph, edge)
		print("adding {} to cost".format(edge))
		cost = cost + float(edge[2]) #add the weight of the edge.
		print("Cost is: {:.2f}".format(cost))
	return cost
# def keyEl(elem):
# 	return elem[2]

# Read in the number of vertices (n) and edges (m)
n = int(input())
m = int(input())

# Read the edges from stdin.
edges = []
for _ in range(m):
    edges.append(input().split())

# Read the A edges. You may want to use a different data-structure.
n_A, A = int(input()), []

#sorting algorithm?
for _ in range(n_A):
	A.append(input().split())

edges.sort(key=elem)
for edge in edges:
	print(edge)
# print("Current Edges:")
# for edge in A:
# 	print(edge)

# print("Possible Edges:")
# print(type(edges))

# edges.sort(key=keyEl)	
# for edge in edges:
# 	print(edge) 

mst_weight = 0.
graph = {}
graph = graph_init(A)
# for k,v in graph.items():
# 	print(k,v)
mst_weight = Kruskal(graph, edges)
# print("Kruskal complete")
# for k,v in graph.items():
# 	print(k,v)

# Print the weight of the mst to two decimal-places. 
print('{:.2f}'.format(mst_weight))