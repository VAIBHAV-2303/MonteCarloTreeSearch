'''

Human player class definition

author: @vaibhav.garg
date: 4th Aug'20
'''

class Human():
	
	def __init__(self, symbol):
		
		self.symbol = symbol

	def getMove(self, board, prevMove):

		print("Enter 2 space separated integers of the form: [0-8] [0-8], corresponding to a valid move ofCourse!")
		
		try:
			move = list(map(int, input().split()))
			return move
		except:
			return self.getMove(board)