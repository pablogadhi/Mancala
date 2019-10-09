import copy
import random

PLAYER_CHOICES_RANGE = list(range(0, 6))
AI_CHOICES_RANGE = list(range(7, 13))


def make_choice(mancala_board, choices_range):
    choices = list(
        filter(lambda x: mancala_board.board[x] != 0, choices_range))
    return random.choice(choices)


def simulate(mancala_board, choice):
    board_copy = copy.deepcopy(mancala_board)
    board_copy.make_move(choice)
    while not board_copy.game_finished:
        c_range = []
        if board_copy.player0_turn:
            c_range = PLAYER_CHOICES_RANGE
        else:
            c_range = AI_CHOICES_RANGE

        board_copy.make_move(make_choice(board_copy, c_range))
    return not board_copy.is_player_winner()


def decide_next_move(mancala_board, simulations):
    choices_score = [0] * len(AI_CHOICES_RANGE)
    for i in range(0, simulations):
        sim_choice = make_choice(mancala_board, AI_CHOICES_RANGE)
        if simulate(mancala_board, sim_choice):
            choices_score[AI_CHOICES_RANGE.index(sim_choice)] += 1

    best_score = max(choices_score)
    return AI_CHOICES_RANGE[choices_score.index(best_score)]
