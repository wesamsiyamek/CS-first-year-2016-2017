import random 
from random import seed, randint
import csv
import matplotlib.pyplot as plt
import math

#Qestion 1.(a)
def game(ra, rb):

	#probability that A wins any given point
	probability_A_wins = ra/(ra+rb)

	#scores for players and winning score set to 11
	A_score = 0
	B_score = 0
	Win_score = 11
	countrallies = 0
	
	seed(57)
	
	#PARS scoring loop
	while (A_score < Win_score and B_score < Win_score) or abs(A_score - B_score) < 2 :
	
		r = random.random()

		if r < probability_A_wins:
			A_score +=1
			countrallies+=1

		else: 
			B_score +=1
			countrallies+=1
	
	#The countrallies is for question 2	
	return(A_score, B_score), countrallies

#Qestion 1.(b)
def winProbability (ra, rb, n):
	
	#counts the number of A winning the games
	counter = 0
	
	for i in range(n):		

		#rallies is for Q2, not related to this function
		results, rallies = game(ra,rb)
		
		if (results[0]>results[1]):
			counter+=1
			
		else:
			pass
	#the number of A winning the games over n the total number of games		
	return round(counter/n,2)

#Qestion 1.(c)
def csv_Reader(filename):

	#opens the csv filename (test.csv)
	with open (filename) as csvfile:

		#creates a list to store the csv data inside it.
		myList = []

		#reads the csv file and assign it to rdr
		rdr = csv.reader(csvfile)

		#skips first row since they don't contain the values that we need
		next(rdr)

		#going through the csv data
		for row in rdr:

			#stores the data inside a tuples and converts str to int
			 mytuple = (int(row[0]), int(row[1]))
			#stores the tuple in the list
			 myList.append(mytuple)

	return myList

#Qestion 1.(d)
def matplot(data_list):
	
	#a list to store the probability of A wins a game against B for each tuple in the data list.
	Prob_plot_list = []
	#a list to store the ra/rb values for each tuple in the data list.
	ra_rb_list=	[]
	#a loop that goes through data_list
	for x in data_list:
	
		#calculates the propability that A wins against B by going through each (ra, rb) in data_list.
		prob_A_wins = x[0]/(x[0]+x[1])
	
		#stores the probabilities for all (ra, rb) in the data_list.
		Prob_plot_list.append(prob_A_wins)
	
		#calculates and store ra/rb of data_list and stores them in ra_rb_list.
		ra_rb_list.append(x[0]/x[1])
	
	#after it exits the loop, it calls the scatter function and gives it the two lists to display it as a figure
	plt.scatter(Prob_plot_list, ra_rb_list)
	
	#represents the y-axis 
	plt.ylabel('Probability A beats B')
	#represents the x-axis
	plt.xlabel('ra/rb')
	#displays the figure 
	plt.show()

#Question 1.(e):
def A_winsGame(ra,rb,n):

	#storing the wins of each player
	A_counter=0
	B_counter=0

	#when players counters are less it goes in the loop and calculates the smallest value of n
	while (A_counter<n) and(B_counter<n):

		#to differentiate between the outputs of game function since it contains rallies for Q2
		scores, rallies =game(ra,rb)

		#counts the wins for each player over range(n) games
		for x in range(n):
			if (scores[x]>scores[x+1]):
				A_counter+=1
			elif(scores[x]<scores[x+1]):
				B_counter+=1
			else:
				continue
				
	return round(ra/(A_counter+ra),1)

#Question 2
def EnglishVsPars(ra, rb):
	#English scoring:-

	#Prob A wins a point
	probability_A_wins = ra/(ra+rb)
	
	#pick first server, if 1: A is server, if 0: B is server
	server_picker = random.randint(0,1)
	
	#stores scores for players 
	A_score = 0
	B_score = 0
	
	#default score 9 could change to 10 somtimes.
	winning_DefaultScore = 9

	countrallies = 0

	#game loop
	while (A_score < winning_DefaultScore and B_score < winning_DefaultScore):
	
		#generates random number to compare with probability_A_wins.
		r = random.random()
	
		#When A is the Server and B is the returner
		if server_picker == 1:
		
			#when A wins a point and continue as a server
			if r < probability_A_wins:
				A_score += 1
				countrallies+=1
		
			#B wins the rally but gains no points, instead becames the server	
			else: 
				server_picker = 0
				countrallies+=1
	
		#when B is the Server and A is the returner		
		else:
		
			#same proccess as the one above
			if r < probability_A_wins:
				server_picker = 1
				countrallies+=1

			else: 
				B_score += 1
				countrallies+=1

		#When both players reaches 8-8
		if (A_score == 8 and B_score < 8):

			#decides if it goes for 9 or 10 points
			nineOrTen = random.randint(9,10)
			#changes the default scores to 9 or 10
			if nineOrTen == 9:
				winning_DefaultScore = 9
			else:
				winning_DefaultScore = 10
		else:
			pass
	
	#after it exits the loop, we use the same abilities value but using the PARS rule in game function.
	pars_score, pars_rallies = game(ra,rb)

	#store the number of rallies for each rule in a list to display it in the figure
	englishrallies = [countrallies]
	parsrallies = [pars_rallies]
	
	plt.bar(englishrallies, 0)
	plt.bar(parsrallies, 0)
	
	# labeling the axis
	plt.ylabel('English rallies')
	plt.xlabel('Pars rallies')
	
	plt.title("English Vs Pars")

	plt.show()
