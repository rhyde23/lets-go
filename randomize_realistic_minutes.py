import random

def close_to_a_goal(goals, proposal) :
	for goal in goals :
		a = abs(goal-proposal)
		if a <= 5 :
			return None 
		if a <= 10 :
			return True 
	return False

def randomize_goals_minutes(number_of_goals) :
	goals = []
	while len(goals) != number_of_goals :
		proposal = random.randint(2, 90)
		if not proposal in goals :
			close = close_to_a_goal(goals, proposal)
			if close == True:
				rando = random.randint(1, 100)
				if rando > 70 :
					goals.append(proposal)
			elif close == False :
				goals.append(proposal)
			
	return goals


	
