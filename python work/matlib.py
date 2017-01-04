"""import matplotlib.pyplot as plt
examMarks = [25, 72, 83, 91, 61]
cwkMarks = [56, 90, 45, 62, 60]
plt.plot(examMarks, cwkMarks)
plt.axes([0, 10, 0, 10])
plt.ylabel('Cwk mark')
plt.xlabel('Exam mark')"""

import random
def test ():
    a= "a"
    if (a == "a"):
        print(1)
    else:
        return 0
#test()

def ParsVsEnglish(ra, rb):
	
	#pars = game(ra,rb)
	
	probability_A_wins = ra/(ra+rb)
	
	#pick first server, if 1: A is server, if 0: B is server
	server_picker = random.randint(0,1)
	
	A_score = 0
	B_score = 0
	
	winning_DefaultScore = 9
 
	while (A_score < winning_DefaultScore or B_score < winning_DefaultScore):

		r = random.random()

		if server_picker == 1:

			if r < probability_A_wins:
				A_score += 1

			else: 
				server_picker == 0

		else:

			if r < probability_A_wins:
				server_picker = 1

			else: 
				B_score += 1

		if (A_score == 8 and B_score < 8):

			nineOrTen = random.randint(9,10)

			if nineOrTen == 9:
				winning_DefaultScore = 9
			else:
				winning_DefaultScore = 10
		
		else:
			pass

	return (A_score, B_score)
 
print(ParsVsEnglish(70,30))