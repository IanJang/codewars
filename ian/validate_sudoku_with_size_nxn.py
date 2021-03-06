'''
[4 kyu] Validate Sudoku with size `NxN`
http://www.codewars.com/kata/validate-sudoku-with-size-nxn/train/python

Given a Sudoku data structure with size NxN, N > 0 and √N == integer, write a method to validate if it has been filled out correctly.
The data structure is a multi-dimensional Array(in Rust: Vec<Vec<u32>>) , ie:
[
  [7,8,4,  1,5,9,  3,2,6],
  [5,3,9,  6,7,2,  8,4,1],
  [6,1,2,  4,3,8,  7,5,9],

  [9,2,8,  7,1,5,  4,6,3],
  [3,5,7,  8,4,6,  1,9,2],
  [4,6,1,  9,2,3,  5,8,7],

  [8,7,6,  3,9,4,  2,1,5],
  [2,4,3,  5,6,1,  9,7,8],
  [1,9,5,  2,8,7,  6,3,4]
]
Rules for validation
Data structure dimension: NxN where N > 0 and √N == integer
Rows may only contain integers: 1..N (N included)
Columns may only contain integers: 1..N (N included)
'Little squares' (3x3 in example above) may also only contain integers: 1..N (N included)
Note: the matrix may include non-integer elements.
'''
import math

from ian import Test


class Sudoku(object):
    def __init__(self, data):
        self.data = data
        self.column_length = len(self.data)
        self.little_square_size = int(math.sqrt(self.column_length))
        self.little_square_sum = int(self.column_length * (self.column_length + 1) / 2)
        self.row_num_of_little_square = int(self.column_length / self.little_square_size)

    def is_valid(self):
        if not self.is_valid_structure():
            return False

        # check row elements
        for i in range(self.column_length):
            row = self.data[i]
            if not self.has_valid_elements(row):
                return False

        # check column elements
        for i in range(self.column_length):
            column = [row[i] for row in self.data]
            if not self.has_valid_elements(column):
                return False

        # check little squares elements
        for i in range(self.row_num_of_little_square):
            sub_little_square_elements = []
            sub_idx = i * self.little_square_size
            for j in range(self.little_square_size):
                sub_little_square_elements.extend(self.data[sub_idx+j][sub_idx:sub_idx+self.little_square_size])
            if not self.has_valid_elements(sub_little_square_elements):
                return False

        return True

    def is_valid_structure(self):
        # little square structure
        if self.little_square_size % 1 != 0:
            return False

        # Whole structure
        for i in range(self.column_length):
            row = self.data[i]
            row_length = len(row)
            if row_length != self.column_length:
                return False
        return True

    def has_valid_elements(self, elements):
        try:
            elements_sum = sum(elements)
            # work-around code for data == [True]
            if elements_sum == 1:
                for element in elements:
                    if type(element) is bool:
                        return False
            if elements_sum == self.little_square_sum:
                if len(set(elements)) == len(elements):
                    return True
        except:
            pass

        return False


def test_validate_sudoku_with_size_nxn():
    # Valid Sudoku
    goodSudoku1 = Sudoku([
        [7, 8, 4, 1, 5, 9, 3, 2, 6],
        [5, 3, 9, 6, 7, 2, 8, 4, 1],
        [6, 1, 2, 4, 3, 8, 7, 5, 9],

        [9, 2, 8, 7, 1, 5, 4, 6, 3],
        [3, 5, 7, 8, 4, 6, 1, 9, 2],
        [4, 6, 1, 9, 2, 3, 5, 8, 7],

        [8, 7, 6, 3, 9, 4, 2, 1, 5],
        [2, 4, 3, 5, 6, 1, 9, 7, 8],
        [1, 9, 5, 2, 8, 7, 6, 3, 4]
    ])

    goodSudoku2 = Sudoku([
        [1, 4, 2, 3],
        [3, 2, 4, 1],

        [4, 1, 3, 2],
        [2, 3, 1, 4]
    ])

    # Invalid Sudoku
    badSudoku1 = Sudoku([
        [0, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],

        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],

        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ])

    badSudoku2 = Sudoku([
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1]
    ])

    Test.it('should be valid')
    Test.assert_equals(goodSudoku1.is_valid(), True, 'Testing valid 9x9')
    Test.assert_equals(goodSudoku2.is_valid(), True, 'Testing valid 4x4')

    Test.it('should be invalid')
    Test.assert_equals(badSudoku1.is_valid(), False, 'Values in wrong order')
    Test.assert_equals(badSudoku2.is_valid(), False, '4x5 (invalid dimension)')

    badSudoku3 = Sudoku([
        [1, 2, 1, 2],
        [3, 4, 3, 4],
        [1, 2, 1, 2],
        [3, 4, 3, 4]
    ])
    Test.it('should be invalid')
    Test.assert_equals(badSudoku3.is_valid(), False, 'Values in wrong order')

    badSudoku4 = Sudoku([
        [1, 2, 3, 4],
        [3, 4, 1, 2],
        [1, 2, 3, 4],
        [3, 4, 1, 2]
    ])
    Test.it('should be invalid')
    Test.assert_equals(badSudoku4.is_valid(), False, 'Values in wrong order')

    badSudoku5 = Sudoku([[True]])
    Test.it('should be invalid')
    Test.assert_equals(badSudoku5.is_valid(), False, 'Values in wrong order')
