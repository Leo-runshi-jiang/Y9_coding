equations={"Math":{"Algebra":[],"Geotrig":[]},"Physics":{"Kinematics":[["v=at","v","a","t"],["a^2+b^2=c^2"],["v","a","t"]],"Mechanics":[]},"Chem":[]}

def findEq(subject,topic,var1,var2,var3,var4,var5):
	equationsList=equations[str(subject)][str(topic)]
	scores=[]
	unsortedScores=[]
	scoreIndex=[]
	#store the scores of each entry in list
	#return(equationsList)
	for i in range(0,len(equationsList)):
		score=0
		if var1 in equationsList[i]:
			score=score+1
		if var2 in equationsList[i]:
			score=score+1
		if var3 in equationsList[i]:
			score=score+1
		if var4 in equationsList[i]:
			score=score+1
		if var5 in equationsList[i]:
			score=score+1
		scores.append(score)
	#get max value index
	sortedScores=scores.copy()
	sortedScores.sort(reverse=True)
	for i in range(0,len(scores)):
		for j, k in enumerate(scores):
			if k == sortedScores[i]and j not in scoreIndex:
				scoreIndex.append(j)

	for i in range(0,len(equationsList)):
		rankedList.append(equationsList[scoreIndex[i]][0])

	output(" ".join(rankedList))
