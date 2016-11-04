#Tant Fant

# class: board 3x3 -- (row,column), initial_board_state 
# with each player has 3 pieces
# 6 pieces - black / white
# loc_list = [elem = player's piece]
# if nothing for that loc, value = ''

# class player -- black player & white player
# has 3 pieces: B1, B2, B3
# white player: W1, W2, W3
# function check if winning -- if theres 3 same color piece in row, column, diagonal
# function make_a_move -- can move to any empty places
# function generate_move & check if reach end state

#  -  -  -
#  -  -  - 
#  -  -  -

class board:
	loc = {}
	def __init__(self) :
		self.loc = ['B', 'B', 'B', '', '', '', 'W', 'W', 'W']
		
	def cur_state(self) :
		return self.loc

	def find_empty_spot(self) :
		return [i + 1 for i, j in enumerate(self.cur_state()) if j == '']

	def set_piece(self, pos, piece) :
		self.loc[pos-1] = piece

	def set_state(self, state) :
		for i in range(len(state)) :
			self.loc[i] = state[i]

	# update the board
	def do_move(self, pos, move, cur_board) :
		empty_spot = cur_board.find_empty_spot()
		cur_piece = cur_board.loc[pos-1]
		update_board = board()
		update_board.set_state(cur_board.cur_state())
		
		if move == 'right' :
			next_pos = pos + 1
			if next_pos in empty_spot :
				update_board.set_piece(pos, '')
				update_board.set_piece(next_pos, cur_piece)
				return update_board
		elif move == 'left' :
			next_pos = pos - 1
			if next_pos in empty_spot :
				update_board.set_piece(pos, '')
				update_board.set_piece(next_pos, cur_piece)
				return update_board
		elif move == 'up' :
			next_pos = pos - 3
			if next_pos in empty_spot :
				update_board.set_piece(pos, '')
				update_board.set_piece(next_pos, cur_piece)
				return update_board
		elif move == 'down' :
			next_pos = pos + 3
			if next_pos in empty_spot :
				update_board.set_piece(pos, '')
				update_board.set_piece(next_pos, cur_piece)
				return update_board
		elif move == 'upleft' :
			next_pos = pos - 4
			if next_pos in empty_spot :
				update_board.set_piece(pos, '')
				update_board.set_piece(next_pos, cur_piece)
				return update_board
		elif move == 'upright' :
			next_pos = pos - 2
			if next_pos in empty_spot :
				update_board.set_piece(pos, '')
				update_board.set_piece(next_pos, cur_piece)
				return update_board
		elif move == 'downleft' :
			next_pos = pos + 2
			if next_pos in empty_spot :
				update_board.set_piece(pos, '')
				update_board.set_piece(next_pos, cur_piece)
				return update_board
		elif move == 'downright' :
			next_pos = pos + 4
			if next_pos in empty_spot :
				update_board.set_piece(pos, '')
				update_board.set_piece(next_pos, cur_piece)
				return update_board
		else :
			return None

    # black piece : 'X'
    # white piece : 'W'
	def print_board(self) :
		next_line = 1
		cur_loc = self.cur_state()
		# print cur_loc
		for pos in cur_loc :
			if pos == 'B' :
				print 'X |',
			elif pos == 'W' :
				print 'O |',
			else :
				print '  |',
			if next_line % 3 == 0 :
				print ""
				print "-----------"
				next_line = 1
			else :
				next_line += 1

class player:

	black_player_pieces = 3
	white_player_pieces = 3
	cur_turn = ''
	move_rules = {1 : ['right', 'down', 'downright',],\
						2 : ['left', 'right', 'down'],\
						3 : ['left', 'down', 'downleft'],\
						4 : ['up', 'down', 'right'],\
						5 : ['up', 'down', 'left', 'right', 'upleft', 'upright', 'downleft', 'downright'],\
						6 : ['left', 'up', 'down'],\
						7 : ['up', 'right', 'upright'],\
						8 : ['up', 'left', 'right'],\
						9 : ['up', 'upleft', 'left']
		}

	def __init__(self) :
		self.cur_turn = 'W'

	def next_turn(self, turn) :
		if turn == 'W' :
			self.cur_turn = 'B'
		else :
			self.cur_turn = 'W'

	def gen_move(self, pos, board) :
		turn = self.cur_turn
		self.next_turn(turn)
		next_moves = self.move_rules[pos]
		return [next_moves, pos, board]

	def primitive(self, cur_board) :
		def all_same_pieces(line) :
			elem = line[0]
			flag = True
			for piece in line :
				if piece != elem :
					flag = False
			return flag

		def who_wins(self) :
			if self.cur_turn == 'W' :
				return 'B'
			else :
				return 'W'

		state = cur_board.cur_state()
		checklists = [[state[0], state[4], state[8]],\
					[state[3], state[4], state[5]],\
					[state[2], state[4], state[6]],\
					[state[0], state[3], state[6]],\
					[state[1], state[4], state[7]],\
					[state[2], state[5], state[8]]]
		res = "UNDECIDED"
		for each_list in checklists :
			if "" in each_list :
				continue
			if all_same_pieces(each_list) == False :
				continue 
			res = who_wins(self)
		return res


def main() :
	print "start Tant Fant"
	tf_board = board()
	tf_player = player()
	tf_board.print_board()
	while True :
		res = tf_player.primitive(tf_board)
		if res != 'UNDECIDED' :
			print res,
			print "WIN!"
			return
		print "which side to play?",
		print tf_player.cur_turn
		pos = input("input your position:")
		next_moves, pos, tf_board = tf_player.gen_move(pos, tf_board)
		print "next_moves: ",
		print next_moves
		move = raw_input("input your move: ")
		tf_board = tf_board.do_move(pos, move, tf_board)
		tf_board.print_board()


	'''
	tant_fant_board = board()
	tant_fant_player = player()
	next_moves, cur_pos, cur_board = tant_fant_player.gen_move(1, tant_fant_board)
	for move in next_moves :
		update_board =  tant_fant_board.do_move(cur_pos, move, cur_board)
		if update_board :
			update_board.print_board()
	'''
			
	print "game over"

main()