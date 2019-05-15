#Program for the Full Simplification of a Polynomial
import math



def reducePoly(cList, eList):
	#Combination of like terms
	for i in range(len(eList)):
		# print("I"+str(i))
		j=i+1
		while j<=len(eList)-1:
			# print(j)
			# print(eList[i],eList[j])
			if eList[i]==eList[j]:
				cList[i] = cList[i]+cList[j]
				del(cList[j])
				del(eList[j])
				reducePoly(cList,eList)
			j+=1

	return cList, eList



def factorPoly(cList, eList):
	factorList = list() #Use to see if factorization is possible
	for i in range(1,1000000):
		factorList.append(i)

	factorables = list() #Factor
	for i in range(len(factorList)):
		if all(x%factorList[i]==0 for x in cList):
			factorables.append(factorList[i])
	maxFactor = max(factorables)
	if maxFactor>1:
		for i in range(len(cList)):
			cList[i]=cList[i]/maxFactor

	return cList, eList, maxFactor



def printSimplifiedPoly(cList,eList,maxFactor):
	print("Simplified Polynomial: ")
	sSimplePoly = str(maxFactor)+'('
	for i in range(len(cList)):
		sSimplePoly=sSimplePoly+str(cList[i])+'x^'+str(eList[i])+'+'
	sSimplePoly=sSimplePoly[:-1]
	sSimplePoly=sSimplePoly+')'
	print(sSimplePoly)



def main():
	#Capture polynomial
	print("Input the polynomial in the csv form 'ax^(j) , bx^(k) , cx^(l) , ...'.\nIf x does not exist (just a constant), use x^0 in it's place.\n")
	sPoly = [x.replace(" ", "") for x in input("Polynomial = ").split(",")]
	print(sPoly)

	#Capture constants and exponents into a list
	cList = list()
	eList = list()
	for i in range(len(sPoly)):
		c = ""
		e = ""
		j = 0

		# constants before x, exponents after ^
		while str(sPoly[i][j])!='x':
			c=c+(sPoly[i][j])
			j+=1
		j+=2 #pass x and ^ characters
		while j<len(sPoly[i]):
			e = e+(sPoly[i][j])
			j+=1

		cList.append(int(c))
		eList.append(int(e))

	cList, eList = reducePoly(cList, eList)
	cList, eList, maxFactor = factorPoly(cList, eList)

	printSimplifiedPoly(cList,eList,maxFactor)

main()