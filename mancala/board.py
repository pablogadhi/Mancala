class Board():
    def __init__(self):
        self.board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
        self.last_position = 0
        self.player0_turn = True

    def make_move(self, position):
        beans = self.board[position]
        for i in range(0, beans):
            next_pos = position + i + 1
            if next_pos >= len(self.board):
                next_pos = next_pos % len(self.board)
            self.board[next_pos] += 1
            self.last_position = next_pos
        self.board[position] = 0
        self.next_turn()

    def next_turn(self):
        if self.last_position == int(len(self.board)/2) - 1 and self.player0_turn:
            return
        elif self.last_position == len(self.board) - 1 and not self.player0_turn:
            return
        self.player0_turn = not self.player0_turn

    def try_to_take_beans(self):
        sub_index = self.last_position % 7
        first_half_val = self.board[:7][sub_index]
        second_half_val = self.board[7:].reverse()[sub_index]
        if first_half_val == 1 and self.last_position < 6:
            pass
        elif second_half_val == 1 and self.last_position > 6:
            pass

    def empty_side(self, start, end):
        for i in range(start, end):
            self.board[end] += self.board[i]
            self.board[i] = 0

    def game_finished(self):
        first_half = self.board[:6]
        second_half = self.board[7:13]
        empty = [0, 0, 0, 0, 0, 0]
        if first_half == empty or second_half == empty:
            self.empty_side(0, 6)
            self.empty_side(7, 13)
            return True
        return False

    def is_player_winner(self):
        if self.board[6] > self.board[13]:
            return True
        return False
