from random import randint 
#sets options
choices=["rock","paper","scissors"]
#ai makes choice

player_lives= 5
computer_lives= 5
computer=choices[randint(0, 2)]

player = False

while player is False:
	print("==============================================================\n")
	print("Computer Lives:", computer_lives, "/5")
	print("Player Lives:", player_lives, "/5")
	print("==============================================================\n")
	player=input("choose rock, paper or scissors: \n")

	#print("computer: ", computer, "player: ", player)
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
			player_lives = player_lives -1
		else:
			print("You Win!", computer, "smashes", player, "\n")
			computer_lives = computer_lives -1

	elif player == "paper":
		if computer == "scissors":
			print("You Lose!", computer, "cuts", player, "\n")
			player_lives = player_lives -1
		else:
			print("You Win!", computer, "covers", player, "\n")
			computer_lives = computer_lives -1		

	elif player == "scissors":
		if computer == "rock":
			print("You Lose!", computer, "smashes", player, "\n")
			player_lives = player_lives -1
		else:
			print("You Win!", computer, "cuts", player, "\n")	
			computer_lives = computer_lives -1	

	if player_lives is 0:
		print("You died, play again?")
		choice = input("Y/N")

		if choice == "y" or choice == "Y":
			player_lives = 5
			computer_lives = 5
			player = False
			computer = choice[randint(0,2)]

		elif choice == "N" or choice == "n":
			print("ByeBye")
			exit()

	if computer_lives is 0:
		print("You win, play again?")
		choice = input("Y/N")

		if choice == "y" or choice == "Y":
			player_lives = 5
			computer_lives = 5
			player = False
			computer = choice[randint(0,2)]

		elif choice == "N" or choice == "n":
			print("ByeBye!")
			exit()

		
	player = False
	computer=choices[randint(0,2)]
