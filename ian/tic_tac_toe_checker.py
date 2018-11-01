"""
http://www.codewars.com/kata/tic-tac-toe-checker/train/python

If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we? Our goal is to create a function that will check that for us!

Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an "X", or 2 if it is an "O", like so:

[[0, 0, 1],
 [0, 1, 2],
 [2, 1, 0]]
We want our function to return:

-1 if the board is not yet finished (there are empty spots),
1 if "X" won,
2 if "O" won,
0 if it's a cat's game (i.e. a draw).
You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.

"""
from ian import KataTest


def isSolved(board):
    ttt = TicTacToe(board)
    return ttt.is_valid()


class TicTacToe:
    DRAW = 0
    NOT_YET_FINISHED = -1
    GAME_OVER_OFFSET = 13

    def __init__(self, board):
        self.board = board
        self.board_size = len(board)
        self.sum_of_elements = 0

    @classmethod
    def check_bingo(cls, row):
        sum_of_row = sum(row)
        num_of_difference_elements = len(set(row))
        if sum_of_row == 0:
            return False
        if num_of_difference_elements == 1:
            return True
        return False

    def is_valid(self):
        # get target rows
        target_rows = []
        for i in range(self.board_size):
            col = [row[i] for row in self.board]
            target_rows.append(col)

            row = self.board[i]
            target_rows.append(row)

            right_down_cross = [self.board[j][j] for j, _row in enumerate(self.board)]
            left_down_cross = [self.board[-j][-j] for j, _row in enumerate(self.board)]
            target_rows.append(right_down_cross)
            target_rows.append(left_down_cross)

            # for check game over
            print(sum(row))
            self.sum_of_elements += sum(row)

        # check bingo from target rows
        for row in target_rows:
            if self.check_bingo(row):
                return row[0]

        if self.is_game_over:
            return self.DRAW
        else:
            return self.NOT_YET_FINISHED

    @property
    def is_game_over(self):
        if self.sum_of_elements < self.GAME_OVER_OFFSET:
            return False
        return True


def test_tic_tac_toc():
    test = KataTest()
    # not yet finished
    board = [[0, 0, 1],
             [0, 1, 2],
             [2, 1, 0]]
    test.assert_equals(isSolved(board), -1)

    # winning row
    board = [[1, 1, 1],
             [0, 2, 2],
             [0, 0, 0]]
    test.assert_equals(isSolved(board), 1)

    # winning column
    board = [[2, 1, 2],
             [2, 1, 1],
             [1, 1, 2]]
    test.assert_equals(isSolved(board), 1)

    # draw
    board = [[2, 1, 2],
             [2, 1, 1],
             [1, 2, 1]]
    test.assert_equals(isSolved(board), 0)

    board = [[1, 2, 0],
             [2, 1, 0],
             [0, 0, 1]]
    test.assert_equals(isSolved(board), 1)
