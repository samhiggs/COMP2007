
#union-find algorithm variables
nodeMap = {}
rank = {}

#file input variables
n = 0 #number of nodes
m = 0 #number of edges
edges = [] #possible edges, as [nodeA, nodeB, weight]
n_A = 0 #number of existing nodes
A = [] #list of existing edges, as [nodeA, nodeB]


#graph variables
graph = {}
mst_weight = 0.

#function to read input file
def read_file():
	n = int(input())
	m = int(input())
	for _ in range(m):
		edges.append(input().split())
	# Read the A edges. You may want to use a different data-structure.
	n_A = int(input())
	for _ in range(n_A):
		A.append(input().split())

#function to sort lists based on value of second tuple. 
def sort():
	edges.sort(key=lambda tpl: tpl[2])

########################################################
#############UNION FIND DATA STRUCTURE##################
########################################################


#initialises a node to its own set.
def makeset(node):
	if node not in nodeMap:
		rank[node] = 0
		nodeMap[node] = node

#returns the root of the node. Used for checking whether 2 nodes are in the same set.
def find(node):
	if nodeMap[node] != node:
		nodeMap[node] = find(nodeMap[node])
	return nodeMap[node]

#merges 2 data structures.
def union(node1, node2):
	root1 = find(node1)
	root2 = find(node2)
	if root1 != root2:
		if rank[root1] < rank[root2]:
			nodeMap[root1] = root2
		else:
			nodeMap[root2] = root1
	if rank[root1] == rank[root2]: rank[root2] += 1

#function to generate a graph
def graph_init():
	graph = {}
	for edge in A:
		add_to_graph(edge)
		makeset(edge[0])
		makeset(edge[1])
		union(edge[0],edge[1])
	return graph  

#adds an edge to the graph and union-find data structure
def add_to_graph(edge):
	if edge[0] in graph:
		graph.get(edge[0]).append(edge[1])
	else:
		graph[edge[0]] = [edge[1]]
		makeset(edge[0])
	if edge[1] in graph:
		graph.get(edge[1]).append(edge[0])
	else: 
		graph[edge[1]] = [edge[0]]
		makeset(edge[1])
	union(edge[0],edge[1])

#a variation of kruskals algorithm. This applies kruskal's algorithm to an existing set.
def kruskal():
	cost = 0
	for edge in edges:
		#checks if they are in the same subset
		if edge[0] in graph and edge[1] in graph:
			if find(edge[0]) == find(edge[1]):
				#checks if path already exists
				if edge[0] in graph[edge[1]]:
					cost += float(edge[2])
				else:
					#we do NOT want to create a cycle
					continue
			#this builds an edge with cut property
			else:
				cost += float(edge[2])
				union(edge[0],edge[1])
		else:
			add_to_graph(edge)
			cost += float(edge[2])
	return cost

##################################
#############MAIN#################
##################################

read_file()
graph_init()
sort()
mst_weight = kruskal()
print('{:.2f}'.format(mst_weight))