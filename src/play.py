'''

File running the main game loop

Author: @vaibhav.garg
Date: 4th Aug'20
'''

from colorama import Fore, Style
from bigBoard import BigBoard
from mcts import MCTS
from human import Human
from copy import *
from randomBot import RandomBot

print(Fore.RED + "Ultimate TicTacToe using Monte Carlo Tree Search")
print(Style.RESET_ALL)

# Initializing game board
board = BigBoard()

# Choose first player
print("Please decide player1")
print("1. MCTS\n2. Human\n3. Random")
choice = input()
if choice == '1':
	p1 = MCTS('X', compTime=0.1)
elif choice == '2':
	p1 = Human('X')
else:
	p1 = RandomBot('X')

# Choose second player
print("Please decide player2")
print("1. MCTS\n2. Human\n3. Random")
choice = input()
if choice == '1':
	p2 = MCTS('O', compTime=0.2)
elif choice == '2':
	p2 = Human('O')
else:
	p2 = RandomBot('O')

# Game loop
board.print()
prevMove = None
while True:

	# P1 turn
	move = None
	validMoves = board.getValidMoves(prevMove)[0]
	while move not in validMoves:
		print("It is P1's turn now.")
		move = p1.getMove(deepcopy(board), prevMove)
	
	board.playMove(move, 'X')
	print("Move played by p1:", move)
	prevMove = move
	board.print()
	curState = board.getState()
	if curState[0] == 'W':
		print("P1 won!")
		break
	elif curState[0] == 'D':
		print("Draw!")
		break

	# P2 turn
	move = None
	validMoves = board.getValidMoves(prevMove)[0]
	while move not in validMoves:
		print("It is P2's turn now.")
		move = p2.getMove(deepcopy(board), prevMove) 
		
	board.playMove(move, 'O')
	print("Move played by p2:", move)
	prevMove = move
	board.print()
	curState = board.getState()
	if curState[0] == 'W':
		print("P2 won!")
		break
	elif curState[0] == 'D':
		print("Draw!")
		break