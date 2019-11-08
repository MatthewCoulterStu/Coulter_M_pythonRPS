from random import randint 
from gameFunctions import winLose, gameVars, comparison


while gameVars.player is False:
	print("==============================================================\n")
	print("Computer Lives:", gameVars.computer_lives, "/",gameVars.total_lives)
	print("Player Lives:", gameVars.player_lives, "/",gameVars.total_lives)
	print("==============================================================\n")
	player=input("choose rock, paper or scissors: \n")

	
	

	
		

	if gameVars.player_lives is 0:
		winLose.winorlose("lost")
		
	if gameVars.computer_lives is 0:
		winLose.winorlose("won")
		

		
	player = False
	gameVars.computer=gameVars.choices[randint(0,2)]
