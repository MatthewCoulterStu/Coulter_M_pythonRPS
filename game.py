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
		print("tie, no one wins! Try again or type quit to exit")

	elif player == "quit":
		print("you chose to quit, goodbye")
		exit()

	elif player == "rock":
		if computer == "paper":
			print("You Lose!", computer, "covers", player, "\n")
		else:
			print("You Win!", computer, "smashes", player, "\n")

	elif player == "paper":
		if computer == "scissors":
			print("You Lose!", computer, "cuts", player, "\n")
		else:
			print("You Win!", computer, "covers", player, "\n")		

	elif player == "scissors":
		if computer == "rock":
			print("You Lose!", computer, "smashes", player, "\n")
		else:
			print("You Win!", computer, "cuts", player, "\n")	
				
		
	player = False
	computer=choices[randint(0,2)]
