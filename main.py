import sys
import curses
import time
from mancala.board import Board
from mancala.ai import decide_next_move

DEBUG_MODE = False


def get_screen(mancala_board):
    board = mancala_board.board
    player_turn = 'Player'
    if not mancala_board.player0_turn:
        player_turn = 'AI'
    return f"""
       {board[12]}  {board[11]}  {board[10]}  {board[9]}  {board[8]}  {board[7]}     Turn: {player_turn}
    {board[13]}                    {board[6]}
       {board[0]}  {board[1]}  {board[2]}  {board[3]}  {board[4]}  {board[5]}
    """.format(board, player_turn)


def print_screen(stdscr, mancala_board):
    if not DEBUG_MODE:
        stdscr.clear()
        stdscr.addstr(0, 0, get_screen(mancala_board))
        stdscr.refresh()
    else:
        print(get_screen(mancala_board))


def start_game(stdscr):
    mancala_board = Board()

    if not DEBUG_MODE:
        curses.use_default_colors()
        curses.curs_set(False)
        curses.init_pair(1, curses.COLOR_MAGENTA, -1)
    print_screen(stdscr, mancala_board)

    while not mancala_board.game_finished():
        if not DEBUG_MODE:
            key = stdscr.getkey()
        else:
            key = input()
        if key == 'q':
            sys.exit(0)
        else:
            try:
                key_as_int = int(key)
                if key_as_int in (1, 2, 3, 4, 5, 6) and mancala_board.board[key_as_int - 1] != 0:
                    mancala_board.make_move(key_as_int - 1)
                    print_screen(stdscr, mancala_board)
                    while not mancala_board.player0_turn and not mancala_board.game_finished():
                        next_move = decide_next_move(mancala_board, 10000)
                        mancala_board.make_move(next_move)
                        print_screen(stdscr, mancala_board)

            except:
                pass

    print_screen(stdscr, mancala_board)
    if not DEBUG_MODE:
        key = stdscr.getkey()


if __name__ == "__main__":
    if not DEBUG_MODE:
        curses.wrapper(start_game)
    else:
        start_game(None)
