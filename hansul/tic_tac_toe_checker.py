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
from hansul import KataTest


def isSolved(board):
    # TODO: Check if the board is solved!
    pass


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
