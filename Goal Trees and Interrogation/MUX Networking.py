#Multiplexor Networking
#Command an LED to be turned on, then a goal tree is printed
import math
from PIL import Image



def printGoals(bLED):
	#Print LED Command
	print("\n~~~\n\nTargetting LED"+str(int(bLED,2)+1))
	#Print M1 Route
	if int(bLED[0])==0:
		print("M1 targetting M2" + " (M1 : "+str(bLED[0])+").")
		#Print M2 Route
		print("M2 targetting LED"+str(int(bLED[1:],2)+1)+" (M2 : "+str(bLED[1:])+").")
	elif int(bLED[0])==1:
		print("M1 targetting M3" + " (M1 : "+str(bLED[0])+").")
		#Print M3 Route
		print("M3 targetting LED"+str(int(bLED[1:],2)+5)+" (M3 : "+str(bLED[1:])+").")



def fillBits(bNum, maxBits):
	while len(bNum)<maxBits:
		bNum = '0'+bNum

	return bNum



def turnOn(bLED):
	b1stM = bLED[0] #address for the first MUX, M1
	b2ndM = bLED[1:] #address for the second MUX, M2 or M3
	img = Image.open("LED"+str(int(bLED,2)+1)+"-ON.png") #The additional "+1" is to account for binary 0 = int 1
	img.show()



def main():
	#Capture User LED ON Request & Process any Errors
	print("Enter LED ON request in the form 'LEDX' where 'X' is an integer 1-8.")
	sLED = input("LED Request: ")
	if len(sLED)!=4:
		print("ERROR: Formatting, Check Input!")
		return
	elif int(sLED[-1])<1:
		print("ERROR: Formatting, Check Input!")
		return
	elif int(sLED[-1])>8:
		print("ERROR: Formatting, Check Input!")
		return
	bLED = bin(int(sLED[-1])-1)
	bLED = fillBits(bLED[2:],3) #3 bits: 1st bit for M1, 2nd/3rd bits for M2 or M3
	
	#Pass Address to printGoals
	printGoals(bLED)

	#Pass Address to turnOn
	turnOn(bLED)


main()