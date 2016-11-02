DRAW = "D"
WIN = "W"
UNDECIDED  ="U"
LOSE = "L"
TIE = "T"

class Piece():
    attributes = None
    full_name = ""
    abbreviation = ""

    def __init__(self, attributes):
        self.attributes = attributes
        if attributes & 0b0001:
            self.full_name += "Tall"
            self.abbreviation += "T"
        else:
            self.full_name += "Short"
            self.abbreviation += "S"
        if attributes & 0b0010:
            self.full_name += " black"
            self.abbreviation += "B"
        else:
            self.full_name += " white"
            self.abbreviation += "W"
        if attributes & 0b0100:
            self.full_name += " circle"
            self.abbreviation += "C"
        else:
            self.full_name += " square"
            self.abbreviation += "Q"
        if attributes & 0b1000:
            self.full_name += " solid-top"
            self.abbreviation += "D"
        else:
            self.full_name += " hollow-top"
            self.abbreviation += "H"
    
    # returns a list of attributes
    def get_attributes(self):
        return self.attributes

    def get_piece_name(self):
        return self.full_name

    def get_piece_abbr(self):
        return self.abbreviation
    
class Board(): 
    pieces = []
    cols_count = 4
    rows_count = 4
    board = None
  
    def __init__(self):
        self.board = [[None for x in range(self.cols_count)] for y in range(self.rows_count)] 
        #short: 0, tall: 1
        #black: 0, white: 1
        #circle: 0, square: 1
        #solid: 0, hollow: 1
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

    def get_pieces(self):
        return self.pieces

    def get_pieces_names(self):
        return ["(" + str(i) + "): " + self.pieces[i].get_piece_name() for i in range(0, len(self.pieces))]
  
    def get_rows(self):
        return self.board
  
    def get_cols(self):
        cols = []
        for row in self.board:
            cols.append([row[i] for i in range(self.rows_count)])
        return cols

    def shared_attributes(self, lst): #finds list of shared attributes among pieces
        attributes_list = [piece.get_attributes() for piece in lst if piece] #nested list of all attributes
        if len(attributes_list) != self.rows_count:
            return 0
        win = 0b1111
        win2 = 0b1111
        for attr in attributes_list:
            win = win & attr
            win2 = win2 & ~attr
        return win or win2
    
    def check_win_horizontal(self):
        for row in self.get_rows(): #0 to 3
            if self.shared_attributes(row): #if there are shared attributes
                return True
        return False

    def check_win_vertical(self):
        attr_list = [[] for i in range(self.rows_count)]
        for row in self.get_rows():
            for i in range(len(row)):
                attr_list[i].append(row[i]) #if there are shared attributes
        for lst in attr_list:
            if self.shared_attributes(lst):
                return True
        return False
       
    def check_win_diagonal(self):
        ltr_diag = []
        rtl_diag = []
        i, j = 0, 3
        for row in self.board:
            ltr_diag += [row[i]]
            rtl_diag += [row[j]]
            i+=1
            j-=1
        if self.shared_attributes(ltr_diag) or self.shared_attributes(rtl_diag):
            return True
        return False
  
    def player(self):
        if len(self.pieces)%2 == 0:
            return 1
        else:
            return 2

    def other_player(self):
        if len(self.pieces)%2 == 0:
            return 2
        else:
            return 1

    def print_board(self):
        for row in self.board:
            pr = []
            for piece in row:
                if piece:
                    pr.append(piece.get_piece_abbr())
                else:
                    pr.append(None)
            print(pr)
  
    def place_piece(self, piece, row, col):
        if not self.board[row][col] and piece in self.pieces:
            self.board[row][col] = piece
            # del self.pieces[piece]
            self.pieces.remove(piece)
            return True
        else:
            return False

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
        return TIE
    return UNDECIDED
  
def gen_moves(state):
  # possible pieces for your opponent to give you
  return state.get_pieces_names()
  
def do_move(move, state):
  #unpack
  # move = (piece, row, col)
  state.place_piece(move[0], move[1], move[2])
  return state

def solve(state):
    return primitive(state)
    
def main():
    print("Starting game of Quarto...")
    print()
    board = initial_position()
    while True:
        print("------------")
        print("Player", board.player(), "'s turn: ")
        print("------------")
        print("Current state of board: ")
        board.print_board()
        print()
        print("Available pieces: ")
        print(gen_moves(board))
        print()
        piece_index = input("Player " +str(board.other_player())+ " please pick a piece to give to Player " + str(board.player()) +" (index num): ")
        p = board.get_pieces()[int(piece_index)]
        print("Player " + str(board.player()) + " choose where you want to place " + p.get_piece_name() + "...")
        r = input("Row: ")
        c = input("Col: ")
        do_move((p,int(r), int(c)), board)
        if solve(board) == WIN:
            board.print_board()
            print("Player", board.other_player(), "wins!")
            return
        else:
            print("SOLVE: ", solve(board))
        print()

main()


    
  
  
  
  
  
  
  
  
    
