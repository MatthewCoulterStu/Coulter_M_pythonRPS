from random import randint 
from gameFunctions import gameVars 
def winorlose(status):
	print("Called win or lose", status)
	print("You", status , "would you like to play again?")
	choice = input("Y/N")

	if choice == "y" or choice == "Y":
		gameVars.player_lives = 5
		gameVars.computer_lives = 5
		gameVars.player = False
		gameVars.computer = gameVars.choices[randint(0,2)]

	elif choice == "N" or choice == "n":
		print("ByeBye")
		exit()
	else:	
		print("make a valid choice. Y or N")
		#recursion calling a function inside itself
		winorlose(status)

#defined function