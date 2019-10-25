from random import randint 
#sets options
choices=["rock","paper","scissors"]
#ai makes choice
computer=choices[randint(0, 2)]

player = False

while player is False:
	player=input("choose rock, paper or scissors: \n")
	print("computer: ", computer, "player: ", player)
	#start doing some logic and condition checking
	#always check a breaking condition first
	if player == computer:
		#we have a tie, no point in going any further
		print("tie, no one wins! Try again")
	elif player == "quit":
		print("you chose to quit, goodbye")
		exit()
	else:
		print("Not a tie. Now we can check other conditions")
		if player == "rock":
			print("check to see what the computer is, a win or a lose")

	player = False
	computer=choices[randit(0,2)]
