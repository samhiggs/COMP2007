
def elem(el):
	return el[2]
def elem2(el):
	return el[0]

# Read in the number of vertices (n) and edges (m)
n = int(input())
m = int(input())

# Read the edges from stdin.
edges = []
for _ in range(m):
    edges.append(input().split())

# Read the A edges. You may want to use a different data-structure.
n_A, A = int(input()), []

for _ in range(n_A):
	A.append(input().split())

	
mst_weight = 0.
print("Ordered by weight")
edges.sort(key=elem)
for edge in edges:
	print(edge)
print("Ordered by source node")
edges.sort(key=elem2)
for edge in edges:
	print(edge)
# Print the weight of the mst to two decimal-places. 
print('{:.2f}'.format(mst_weight))