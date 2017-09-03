nodeSet = {}
def makeset(node):
    nodeSet[node] = node

def union(nodeA, nodeB):
    if(nodeSet[nodeA] != nodeA):
        nodeSet[nodeA] = nodeB
    else:
        nodeSet[nodeB] = nodeA

#returns the set that the node belongs to.        
def find(node):
    return nodeSet[node]
    




nodesRaw = [0,1,2,3,4,5,6,7,8,9]
for node in nodesRaw:
    makeset(node)

for node in nodesRaw:
    print(find(node))

union(0,6)
union(0,1)
union(0,4)
union(5,6)
print("lets look at the post union nodes")
for k,v in nodeSet.items():
    print(k,v)