#Program for Solving 3D Trigonometry Problems
#User inputs 3 points in 3D space, program outputs the triangles dimensions
#Side lengths, angles, triangle area
import math



def calcSideLength(pointA, pointB):
	#x difference squared
	xDS = pow((pointB[0]-pointA[0]),2)
	#y difference squared
	yDS = pow((pointB[1]-pointA[1]),2)
	#z difference squared
	zDS = pow((pointB[2]-pointA[2]),2)
	#side length
	sL = math.sqrt(xDS+yDS+zDS)
	
	return sL



def calcAngles(sAB, sBC, sAC):
	#Calculate angles (RADIANS) using law of cosines and sumAngles=pi=3.14159
	#cos(A) = (sAB^2 + sAC^2 - sBC^2)/(2*AB*AC)
	#A = arccos((sAB^2 + sAC^2 - sBC^2)/(2*AB*AC))
	aCAB = math.acos((pow(sAB,2) + pow(sAC,2) - pow(sBC,2))/(2*sAB*sAC)) #angle for corner A
	aBCA = math.acos((pow(sBC,2) + pow(sAC,2) - pow(sAB,2))/(2*sBC*sAC)) #corner B
	aABC = math.pi-aBCA-aCAB #corner C

	return aABC, aBCA, aCAB



def triArea(sAC, sBC, aBCA):
	#Use the side-angle-side method
	Area = ((sAC*sBC*math.sin(aBCA))/2)

	return Area



def main():
	#Capture points
	print("Input the requested data in the form 'x,y,z'.\n")
	pA = [int(x) for x in input("Point A: ").split(',')]
	pB = [int(x) for x in input("Point B: ").split(',')]
	pC = [int(x) for x in input("Point C: ").split(',')]

	#Calculate side lengths
	sAB = calcSideLength(pA, pB)
	sBC = calcSideLength(pB, pC)
	sAC = calcSideLength(pA, pC)

	#Calculate angles
	aABC, aBCA, aCAB = calcAngles(sAB,sBC,sAC)

	#Calculate area
	Area = triArea(sAC, sBC, aBCA)
	print("Area = ", Area)



main()