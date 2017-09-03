

nodeSet = {}
def makeset(node):
    nodeSet[node] = node

def union(nodeA, nodeB):
    #I Need to find the root of the nodes to unionise.
    rootA = find(nodeA)
    rootB = find(nodeB)
    if(rootA != rootB):
    	nodeSet[rootA] = rootB


#returns the set that the node belongs to.        
def find(node):
    while nodeSet[node] != node:
        return find(nodeSet[node])
    return node
    




nodesRaw = [0,1,2,3,4,5,6,7,8,9]

for node in nodesRaw:
    makeset(node)
#set 1
union(0,6)
union(0,1)
union(0,4)
#set 2
print("finding 5")
print(find(5))
union(5,7)
print(nodeSet.get(5))
print(nodeSet.get(7))
union(5,8)
union(8,9)
union(8,2)
print(find(7))
print(find(8))
# union(0,5)#This is an important edge case to consider.
print("node {} root is: {}".format(1,find(1)))
print("node {} root is: {}".format(2,find(2)))
print("lets look at the post union nodes")
for k,v in nodeSet.items():
    print(k,v)