DRAW = "D"
WIN = "W"
UNDECIDED  ="U"
LOSE = "L"
TIE = "T"

class Piece():
  attributes = None
	def __init__(self, attributes):
		self.attributes = attributes
    
  # returns a list of attributes
  def get_attributes(self):
    return self.attributes
    
class Board(): #[[None None 0 0], [0 0 0 0], [0 0 0 0], [0 0 0 0 ]]
  	pieces = []
  	cols_count, rows_count = 4
  	board = None
  
	def __init__(self):
		self.board = [[None for x in range(cols_count)] for y in range(rows_count)] 
	    #short: 0
	    #black: 0
	    #circle: 0
	    #solid: 0
	    self.pieces.append(Piece(0b0000))
	    self.pieces.append(Piece(0b0001))
	    self.pieces.append(Piece(0b0010))
	    self.pieces.append(Piece(0b0011))
	    self.pieces.append(Piece(0b0100))
	    self.pieces.append(Piece(0b0101))
	    self.pieces.append(Piece(0b0110))
	    self.pieces.append(Piece(0b0111))
	    self.pieces.append(Piece(0b1000))
	    self.pieces.append(Piece(0b1001))
	    self.pieces.append(Piece(0b1010))
	    self.pieces.append(Piece(0b1011))
	    self.pieces.append(Piece(0b1100))
	    self.pieces.append(Piece(0b1110))
	    self.pieces.append(Piece(0b1101))
	    self.pieces.append(Piece(0b1111))

	def get_board(self):
		return self.board
  
  	def get_rows(self):
    	return self.board
  
  	def get_cols(self):
    	cols = []
    	for row in self.board:
      		cols.append([row[i] for i in range(rows_count)])
    	return cols

	def shared_attributes(self, lst): #finds list of shared attributes among pieces
    	attributes_list = [piece.get_attributes() for piece in lst if piece] #nested list of all attributes
		if len(attributes_list) != rows_count:
      		return 0
    	win = 0b1111
    	for attr in attributes_list:
      		win = win & attr
    	return win
    
  	def check_win_horizontal(self):
    	for row in get_rows(): #0 to 3
      		if shared_attributes(row): #if there are shared attributes
        		return WIN
    	return UNDECIDED

  	def check_win_vertical(self):
    	for col in get_cols():
      		if shared_attributes(col): #if there are shared attributes
          		return WIN
    	return UNDECIDED
       
  	def check_win_diagonal(self,state):
      	ltr_diag, rtl_diag = []
      	i, j = 0, 3
      	for row in self.board:
        	ltr_diag += [row[i]]
        	rtl_diag += [row[j]]
        	i+=1
        	j-=1
      	if shared_attributes(ltr_diag) or shared_attributes(rtl_diag):
        	return WIN
      	return UNDECIDED
  
  	def player(self):
    	if len(self.pieces)%2 == 0 return 1
   		else return 2
  
  	def place_piece(self, piece, row, col):
    	self.board[row][col] = piece
   		# del self.pieces[piece]
   		self.pieces.remove(piece)
    	return self.board

quarto_board = None	

def initial_position():
	# 2d array: 4x4 initialized to 
	return Board() 

# takes in a 4x4 array - state is of class Board
def primitive(state):
	if state.check_win_horizontal() or state.check_win_vertical() or state.check_win_diagonal():
		return WIN
	# no more pieces
	if len(state.pieces) == 0:
		return LOSE
	return UNDECIDED
  
def gen_moves(state):
  # possible pieces to give to your opponent
  return state.pieces
  
def do_move(move, state):
  #unpack
  state.place_piece(move)
    
                  
	
  
  
  
  
  
  
  
  
    
