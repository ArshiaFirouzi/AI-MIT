# Depth First Search Algorithm
# S is the start point, E in the target end

# import networkx as nx
# import matplotlib.pyplot as plt
import time
import random
import string



class node:

	def __init__(self, name, neighbors, position):
		self.name = name #String
		self.neighbors = neighbors #List of strings (node names)
		self.position = position #2nd order list of this node's xy-position

	def addNeighbor(self,nName):
		nName = str(nName)
		self.neighbors.append(nName)
		print(f"Neighbor {nName} added.")



class nodeNetwork:

	def __init__(self, nodes):
		self.nodes = nodes
		self.numNodes = len(nodes)

	def addNode(self, nodeName, nodeNeighbors, nodePosition):
		newNode = node(nodeName, nodeNeighbors, nodePosition)
		self.nodes.append(newNode)
		print(f"Node {self.nodes[-1].name} added!")

	def getNodeNeighbors(self, nName):
		for i in range(len(self.nodes)):
			if str(self.nodes[i].name) == str(nName):
				return self.nodes[i].neighbors

	def getNodePosition(self, nName):
		for i in range(len(self.nodes)):
			if str(self.nodes[i].name) == str(nName):
				return self.nodes[i].position



#Input is a network of nodes, queue of nodes to be searched, stop if the end node is ever reached
def DFS(nN, queue, tries, sNodes):

	#Capture parent node
	# print(f"\nQueue: {queue}")
	parentNode = (queue[0].split(','))[-1]
	# print(f"Parent Node: {parentNode}")

	#Create parent's new path
	newPaths = nN.getNodeNeighbors(parentNode)
	# print(f"New path: {newPaths}")

	tempList = []
	#Add new path to queue
	for i in range(len(newPaths)):
		if newPaths[i] not in sNodes:
			sNodes.append(newPaths[i])
		elif newPaths[i] in sNodes:
			# print(f"Searched Nodes: {sNodes}")
			continue
		tempList.append(queue[0]+","+newPaths[i])
		#Test for success
		splitPath = newPaths[i].split(',')
		if 'E' in splitPath:
			# print(f"\nFOUND, in {tries} tries!!! {newPaths[i]}\n\n")
			return newPaths[i], tries
	# print(f"Temp List: {tempList}")
	queue = queue[1:]
	queue = tempList + queue

	tries+=1

	if tries>=100:
		# print(f"\n\nSearched Nodes: {sNodes}")
		return 'Fail', tries
	else:
		successPath, tries = DFS(nN, queue, tries, sNodes)

	return successPath, tries





def main():

	#Start Time
	sT = time.time()

	# Create network matching the image: 'Search Space.png'
	# Networks can easily be created using the random package and a dictionary of names matching node neighbors and position
	nS = node('S',['6','7','8','9'],(0,0))
	n1 = node('1',['4'],(-2,1.5))
	n2 = node('2',['4','5'],(-2,0.75))
	n3 = node('3',['7'],(-1,-1))
	n4 = node('4',['1','2','6'],(-1,1))
	n5 = node('5',['2','6','7'],(-1,0))
	n6 = node('6',['4','5','8','S'],(-0.5,0.5))
	n7 = node('7',['3','5','S'],(-0.5,-0.75))
	n8 = node('8',['6','S','10'],(0,1))
	n9 = node('9',['11','12','S'],(0.75,-0.5))
	n10 = node('10',['8','12','E'],(1,1))
	n11 = node('11',['9','12'],(1.5,-1))
	n12 = node('12',['9','10','11','E'],(1.5,-0.25))
	nE = node('E',['10','12'],(1.75,1.5))
	nodes = [nS,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12]

	# Init network
	nNetwork = nodeNetwork(nodes)

	# Create BMS list of paths
	queue = [nNetwork.nodes[0].name]
	dfsPath, tries = DFS(nNetwork, queue, 0, ['S'])

	# #Check for success
	if dfsPath == 'Fail':
		print("\nFAILURE!")
		print(f"Path not found in {tries} tries.\n")
	else:
		print("\nSUCCESS!")
		print(f"Path = {dfsPath} :: Found in {tries+1} tries.\n")

	eT = time.time()
	print(f"Elapsed Time: {eT-sT}\n")




main()