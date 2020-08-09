'''

SmallBoard class definition

author: @vaibhav.garg
date: 4th Aug'20
'''

class SmallBoard():
	
	def __init__(self):

		self.board = [['_', '_', '_'],
					  ['_', '_', '_'],
					  ['_', '_', '_']]

	def getAllEmptySlots(self):

		slots = []
		if self.getState()[0] == 'N':
			for i in range(3):
				for j in range(3):
					if self.board[i][j] == '_':
						slots.append([i, j])
		return slots

	def playMove(self, move, symbol):

		self.board[move[0]][move[1]] = symbol

	def getState(self):

		# Horizontal check
		for i in range(3):
			if self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2] and self.board[i][0] != '_':
				return 'W', self.board[i][0]

		# Vertical check
		for i in range(3):
			if self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i] and self.board[0][i] != '_':
				return 'W', self.board[0][i]

		# Diagonal check
		if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[0][0] != '_':
			return 'W', self.board[0][0]
		if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and self.board[0][2] != '_':
			return 'W', self.board[0][2]

		# Draw Check
		for i in range(3):
			for j in range(3):
				if self.board[i][j] == '_':
					return 'N', '_'
		return 'D', '_'

	def print(self):

		for i in range(3):
			for j in range(3):
				print(self.board[i][j], end=' ')
			print()