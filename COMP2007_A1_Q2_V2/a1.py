from collections import deque
import heapq

#union-find algorithm variables
parent = {}
rank = {}

#file input variables
n = 0 #number of vertices
m = 0 #number of edges
edges = [] #possible edges, as [nodeA, nodeB, weight]
n_A = 0 #number of existing nodes
A = [] #list of existing edges, as [nodeA, nodeB]


#graph variables
graph = {}
mst_weight = 0.

def read_file():
	n = int(input())
	m = int(input())
	for _ in range(m):
		edges.append(input().split())
	# Read the A edges. You may want to use a different data-structure.
	n_A = int(input())
	for _ in range(n_A):
		A.append(input().split())

def make_set(vertice):
	if vertice not in parent:
		parent[vertice] = vertice
		rank[vertice] = 0

def find(vertice):
	if parent[vertice] != vertice:
		parent[vertice] = find(parent[vertice])
	return parent[vertice]

def union(vertice1, vertice2):
	root1 = find(vertice1)
	root2 = find(vertice2)
	if root1 != root2:
		if rank[root1] > rank[root2]:
			parent[root2] = root1
		else:
			parent[root1] = root2
	if rank[root1] == rank[root2]: rank[root2] += 1

def print_unionfind_parent():
	for k,v in parent.items():
		print(k,v)

def add_to_graph(edge):
	if edge[0] in graph:
		graph.get(edge[0]).append(edge[1])
	else:
		graph[edge[0]] = [edge[1]]
		make_set(edge[0])
	if edge[1] in graph:
		graph.get(edge[1]).append(edge[0])
	else: 
		graph[edge[1]] = [edge[0]]
		make_set(edge[1])
	union(edge[0],edge[1])
#function to generate a graph
def graph_init():
	graph = {}
	for edge in A:
		add_to_graph(edge)
		make_set(edge[0])
		make_set(edge[1])
		union(edge[0],edge[1])
	return graph  

def print_graph():
	for k,v in graph.items():
		print(k,v)

def print_possible_edges():
	for edge in edges:
		print(edge)

def print_existing_edges():
	for edge in A:
		print(edge)

def sort():
	edges.sort(key=lambda tup: tup[2])

def kruskal():
	cost = 0
	costs = []
	for edge in edges:
		# print(edge)
		# if(edge[0] == 0 and edge[1] == 3):
		# 	print("EDGE")
		#checks if they are in the same subset
		if edge[0] in graph and edge[1] in graph:
			# print("Vertice {} and Vertice {} has weight {}".format(edge[0],edge[1], edge[2]))
			# print(find(edge[0]) == find(edge[1]))
			if find(edge[0]) == find(edge[1]):
				#checks if path already exists
				if edge[0] in graph[edge[1]]:
					cost += float(edge[2])
					costs.append(edge[2])
				else:
					#we cannot create a cycle
					continue
			else:
				cost += float(edge[2])
				costs.append(edge[2])
				union(edge[0],edge[1])
		else:
			add_to_graph(edge)
			cost += float(edge[2])
			costs.append(edge[2])
	# print(costs)
	return cost

##################################
#############MAIN#################
##################################

read_file()
graph_init()
sort()
# print_possible_edges()
# print_existing_edges()
# print("Here is da graph:")
mst_weight = kruskal()
# print_graph()
# print_unionfind_parent()

# #this could probably be better but hail modularity.
# edges.sort(key=elem)
# for edge in edges:
# 	print(edge)

# graph = graph_init(A)
# # for k,v in graph.items():
# # 	print(k,v)
# mst_weight = Kruskal(graph, edges)
# # print("Kruskal complete")
# # for k,v in graph.items():
# # 	print(k,v)

# # Print the weight of the mst to two decimal-places. 
print('{:.2f}'.format(mst_weight))