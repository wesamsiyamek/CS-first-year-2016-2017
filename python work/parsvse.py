import random
def ParsVsEnglish(ra, rb):
	
	#pars = game(ra,rb)
	
	probability_A_wins = ra/(ra+rb)
	
	#pick first server, if 1: A is server, if 0: B is server
	server_picker = random.randint(0,1)
	
	A_score = 0
	B_score = 0
	
	winning_DefaultScore = 9
	
	while (A_score < winning_DefaultScore and B_score < winning_DefaultScore):
		
		r = random.random()
		
		if server_picker == 1:
			
			if r < probability_A_wins:
				A_score += 1
				
			else: 
				server_picker = 0
				
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

	print(A_score,B_score)

	"""print(A_score, B_score, pars[0], pars[1])		
	plt.plot([A_score, B_score], [pars[0], pars[1]])
	plt.ylabel('English Scoring')
	plt.xlabel('PAR Scoring')
	plt.show()"""
