import networkx as nx
import matplotlib.pyplot as plt
import time
import random
import string




def spawnBlocks(n): # 0 <= n <= 12

	G = nx.Graph()
	pos = dict()
	blocks = list()
	letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m"]	# Node names
	for i in range(n):
		G.add_node(letters[i])
		pos[str(letters[i])] = ((n-i),0)
		blocks.append(str(letters[i]))
	G.add_node("TopLeft")
	pos["TopLeft"] = (0,n+1)
	G.add_node("TopRight")
	pos["TopRight"] = (n+1,n+1)
	G.add_node("BotLeft")
	pos["BotLeft"] = (0,-1)
	G.add_node("BotRight")
	pos["BotRight"] = (n+1,-1)

	return G, pos, blocks



def capAction(action, blocks): # action is a string with form 'a ON b' or 'EXIT'
	action = action.lower()

	if (len(action)==6 and ((action[0] in blocks) and (action[-1] in blocks))):
		print("ACCEPTED: " + str(action))
		return action

	elif action=="exit":
		print("ACCEPTED: " + str(action) + "\n")
		return "CMD : EXIT"

	else:
		print("NOT ACCEPTED: " + str(action) + "\n")
		return "CMD : PASS"



def popTop(G,block,avoid,pos,blocks,target):	

	# Get to top non-target block
	if (pos[block][0],pos[block][1]+1) in pos.values():
		for kvPair in pos:
			if pos[kvPair] == (pos[block][0],pos[block][1]+1):
				block = kvPair
				G, pos, block = popTop(G, block, avoid, pos, blocks, target)

	elif (block!=target): # If this is not the target block, raise, shift, and drop it
		xCoo = pos[block][0]

		# Raise it
		del(pos[block])
		pos[block] = (xCoo,len(blocks))
		plt.close()
		time.sleep(0.01)
		nx.draw(G, pos, with_labels=True)
		plt.show()
		plt.pause(0.01)
		time.sleep(.5)	

		# Shift it
		if xCoo>2: # shift left
			xCoo = xCoo-1
			if xCoo==avoid:
				xCoo = xCoo-1
		else: # shift right
			xCoo = xCoo+1
			if xCoo==avoid:
				xCoo = xCoo+1
		del(pos[block])
		pos[block] = (xCoo,len(blocks))
		plt.close()
		time.sleep(0.01)
		nx.draw(G, pos, with_labels=True)
		plt.show()
		plt.pause(0.01)
		time.sleep(.5)

		# Drop it
		yCoo = pos[block][1]
		while True:
			if ((pos[block][0],pos[block][1]-1) not in pos.values()) and (pos[block][1]-1 != -1): #nothing under the block, lower it one space
				yCoo-=1
				del(pos[block])
				pos[block] = (xCoo,yCoo)
				plt.close()
				time.sleep(0.01)
				nx.draw(G, pos, with_labels=True)
				plt.show()
				plt.pause(0.01)
				time.sleep(.2)
			else: #something under it, break as we have dropped the block
				break

	return G, pos, block



def moveBlock(G,block,pos,blocks,targetBlock): # moves topBlock onto botBlock (both blocks must be uncovered first!)

	xCoo = pos[block][0]
	yCoo = pos[block][1]

	# Raise it
	yCoo = len(blocks)
	del(pos[block])
	pos[block] = (xCoo,yCoo)
	plt.close()
	time.sleep(0.01)
	nx.draw(G, pos, with_labels=True)
	plt.show()
	plt.pause(0.01)
	time.sleep(.5)	

	# Shift it
	xCoo = pos[targetBlock][0]
	del(pos[block])
	pos[block] = (xCoo,yCoo)
	plt.close()
	time.sleep(0.01)
	nx.draw(G, pos, with_labels=True)
	plt.show()
	plt.pause(0.01)
	time.sleep(.5)

	# Drop it
	while True:
		if ((pos[block][0],pos[block][1]-1) not in pos.values()) and (pos[block][1]-1 != -1): #nothing under the block, lower it one space
			yCoo-=1
			del(pos[block])
			pos[block] = (xCoo,yCoo)
			plt.close()
			time.sleep(0.01)
			nx.draw(G, pos, with_labels=True)
			plt.show()
			plt.pause(0.01)
			time.sleep(.2)
		else: #something under it, break as we have dropped the block
			break

	return G, pos



def main():

	#Generate block arrangement (5 blocks)
	G, pos, blocks = spawnBlocks(5)
	nx.draw(G, pos, with_labels=True)
	plt.show(block=False)
	plt.ion()
	plt.plot()
	plt.pause(0.01)

	while True:

		#Capture user input to place a block on another, "EXIT" to stop loop and thus the program
		print("Placement Command Form: 'a ON b'")
		print("Input 'EXIT' to end program.")
		action = capAction(input("Action: "), blocks)
		if action == "CMD : PASS":
			print("PASSED")
			continue
		elif action == "CMD : EXIT":
			break
		topBlock = action[0].lower()
		botBlock = action[-1].lower()

		#Cleartop of both blocks, start with topblock, avoid x-coordinate of other block (avoid)
		avoid = pos[str(botBlock)][0]
		block = topBlock
		G, pos, block = popTop(G,topBlock,avoid,pos,blocks,topBlock)
		if block!=topBlock:
			i=0
			while block!=topBlock:
				G, pos, block = popTop(G,topBlock,avoid,pos,blocks,topBlock)
		avoid = pos[str(topBlock)][0]
		block = botBlock
		G, pos, block = popTop(G,botBlock,avoid,pos,blocks,botBlock)
		if block!=botBlock:
			i=0
			while block!=botBlock:
				G, pos, block = popTop(G,botBlock,avoid,pos,blocks,botBlock)

		#Moveblock
		G, pos = moveBlock(G,topBlock,pos,blocks,botBlock)



main()