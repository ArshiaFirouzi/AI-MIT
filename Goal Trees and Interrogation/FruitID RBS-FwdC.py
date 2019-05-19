#Rule based system for identifying fruit (Orange v Apple v Banana v Grapes v Watermelon v Lemon)
#Forward chaining version
import math
import string



class rbsFruit:

	def __init__(self):
		
		# Rules of Form: if,then OR(x,y,z,...)
		R0 = "Peel", "Orange,Banana,Watermelon,Lemon"
		R1 = "Green", "Apple,Grapes,Watermelon"
		R2 = "Red", "Apple,Grapes"
		R3 = "Yellow", "Banana,Lemon"
		R4 = "Crunchy", "Apple,Watermelon"
		R5 = "Sectioned", "Orange,Lemon"
		R6 = "Orange", "Orange"
		self.Rs = (R0,R1,R2,R3,R4,R5,R6)
		self.keyRs = (R0[0],R1[0],R2[0],R3[0],R4[0],R5[0],R6[0])
		# Chars already input, starts empty - grows as chars are set. Objective is to reduce redundancy
		self.setChars = list()
		# Possibilities are the potential fruits that may be being described based on input characteristics
		self.possibilities = ['Orange', 'Apple', 'Banana', 'Grapes', 'Watermelon', 'Lemon']

		print("rbsFruit Initialized")

	def setChar(self, char):
		if char in self.setChars:
			print("Already a characteristic!")
			return '!'
		elif char not in self.keyRs:
			print("Not an acceptable characteristic!")
			return '!'

		self.setChars.append(char)
		return ':)'


	def checkRules(self): #check to see if the new characteristic (last item in setChars) makes this a fruit
		newPoss = list()
		tempPoss = list()
		rule = self.setChars[-1] # Newest characteristic
		for i in range(len(self.Rs)):
			if rule == self.Rs[i][0]:
				newPoss = self.Rs[i][1].split(',')
		for i in range(len(self.possibilities)):
			for j in range(len(newPoss)):
				if self.possibilities[i] == newPoss[j]:
					tempPoss.append(self.possibilities[i])

		self.possibilities = tempPoss

		if len(tempPoss) == 0:
			print("Fruit unidentifiable!")
			return '!'
		elif len(tempPoss) == 1:
			print("You are describing a/an " + str(tempPoss[0]) + "!")
			return '!'
		else:
			self.possibilities = tempPoss
			return ':)'


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def main():

	fruit = rbsFruit()

	while True:

		#Capture characteristic from user
		print("Input a characteristic of the fruit, acceptable inputs are : Peel, Green, Red, Yellow, Crunchy, Sectioned.")
		characteristic=input("Input: ")
		
		if characteristic == 'exit': # User wants to exit
			break

		if fruit.setChar(characteristic) == '!': # Input is not acceptable
			continue

		#At this point an input characteristic was accepted and saved, time to see if we have a fruit identified
		if fruit.checkRules() == '!': # Fruit identified or unidentifiable
			break

		print("Current possibilities: " + str(fruit.possibilities))

main()