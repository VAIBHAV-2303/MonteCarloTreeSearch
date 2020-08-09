'''

Random player class definition

author: @vaibhav.garg
date: 8th Aug'20
'''

import random

class RandomBot():
	
	def __init__(self, symbol):
		
		self.symbol = symbol

	def getMove(self, board, prevMove):

		nextMoves, nextSymbol = board.getValidMoves(prevMove)

		return random.choice(nextMoves)