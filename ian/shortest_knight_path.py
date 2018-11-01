"""
[4 kyu] Shortest Knight Path

https://www.codewars.com/kata/shortest-knight-path/train/python

Given two different positions on a chess board, find the least number of moves it would take a knight to get from one to the other. The positions will be passed as two arguments in algebraic notation. For example, knight("a3", "b5") should return 1.

The knight is not allowed to move off the board. The board is 8x8.

For information on knight moves, see https://en.wikipedia.org/wiki/Knight_%28chess%29

For information on algebraic notation, see https://en.wikipedia.org/wiki/Algebraic_notation_%28chess%29

(Warning: many of the tests were generated randomly. If any do not work, the test cases will return the input, output, and expected output; please post them.)
"""
from ian import Test


def knight(p1, p2):
    # start here!
    pass


def test_shortest_knight_path():
    arr = [['a1', 'c1', 2], ['a1', 'f1', 3], ['a1', 'f3', 3], ['a1', 'f4', 4], ['a1', 'f7', 5]]
    for x in arr:
        z = knight(x[0], x[1])
        Test.expect(z == x[2], "{} to {}: expected {}, got {}".format(x[0], x[1], x[2], z))
