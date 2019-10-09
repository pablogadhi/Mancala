import sys
import curses
import time
from mancala.board import Board
from mancala.ai import decide_next_move


def get_screen(board):
    return f"""
       {board[12]}  {board[11]}  {board[10]}  {board[9]}  {board[8]}  {board[7]}
    {board[13]}                    {board[6]}
       {board[0]}  {board[1]}  {board[2]}  {board[3]}  {board[4]}  {board[5]}
    """.format(board)


def print_screen(stdscr, mancala_board):
    stdscr.clear()
    stdscr.addstr(0, 0, get_screen(mancala_board.board))
    stdscr.refresh()


def start_game(stdscr):
    mancala_board = Board()

    curses.use_default_colors()
    curses.curs_set(False)
    curses.init_pair(1, curses.COLOR_MAGENTA, -1)
    print_screen(stdscr, mancala_board)

    while True:
        key = stdscr.getkey()
        if key == 'q':
            sys.exit(0)
        else:
            try:
                key_as_int = int(key)
                if key_as_int in (1, 2, 3, 4, 5, 6) and mancala_board.board[key_as_int - 1] != 0:
                    mancala_board.make_move(key_as_int - 1)
                    print_screen(stdscr, mancala_board)
                    if not mancala_board.player0_turn:
                        next_move = decide_next_move(mancala_board, 10000)
                        mancala_board.make_move(next_move)
                        time.sleep(0.5)
                        print_screen(stdscr, mancala_board)
                    if mancala_board.game_finished():
                        sys.exit(0)

            except:
                pass


if __name__ == "__main__":
    curses.wrapper(start_game)
