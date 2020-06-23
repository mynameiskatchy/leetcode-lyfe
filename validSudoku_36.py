
""" Could be improved way more & needs to check 3x3 square
====================================================================================================
36. Valid Sudoku
validSudoku()
<https://leetcode.com/problems/valid-sudoku/>
<https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/769/>
====================================================================================================

Determine if a 9x9 Sudoku board is valid.
Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid. <SEE ACTUAL PAGE FOR IMAGE>

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:
----------
Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true

Example 2:
----------
Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Note:
-----
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.

"""


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool

        needs to check 3x3 square is valid
        """

        def is_duplicates(items):
            """ Check if list contains duplicates
            :type items: List[str]
            :rtype: bool
            """
            d = {}
            
            for j, val in enumerate(items):
                if val != ".":
                    if val in d:
                        return True
                    else:
                        d[val] = 1
            return False

        def get_columns(board):
            """ Make a board with easier to access columns
            :type board: List[List[str]]
            rtype: Dict[str]
            """
            d = {}
            
            for j in range(9):
                temp = []
                for i, row in enumerate(board):
                    temp.append(row[j])
                    d[j] = temp
            return d
        
        def convert_to_dict(board):
            """ Make board with easier to access rows
            :type board: List[List[str]]
            rtype: Dict[str]
            """
            d = {i:val for i, val in enumerate(board)}
            return d

        m = convert_to_dict(board)
        n = get_columns(board)

        for i in range(9):
            if is_duplicates(m[i]) == True or is_duplicates(n[i]) == True:
                return False
        return True

    

    def isValidSudoku2(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool

        470 / 504 test cases passeda.
        
        needs to check 3x3 square is valid
        """

        m = {}
        n = {}

        for i in range(9):
            col = []
            for row in board:
                col.append(row[i])
            m[i] = board[i]
            n[i] = col

        def contains_dupes(values):
            count = {}
            for i in values:
                if i != '.':
                    if i not in count.keys():
                        count[i] = 1
                    else:
                        return True
            return False
        
        count_m = {}
        for i in m.values():
            if contains_dupes(i):
                return False
        for i in n.values():
            if contains_dupes(i):
                return False
        return True


if __name__ == "__main__":
    input1 = \
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]

    input2 = \
        [
            ["8","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]

    input3 = \
        [
            [".",".",".",".","5",".",".","1","."],
            [".","4",".","3",".",".",".",".","."],
            [".",".",".",".",".","3",".",".","1"],
            ["8",".",".",".",".",".",".","2","."],
            [".",".","2",".","7",".",".",".","."],
            [".","1","5",".",".",".",".",".","."],
            [".",".",".",".",".","2",".",".","."],
            [".","2",".","9",".",".",".",".","."],
            [".",".","4",".",".",".",".",".","."]]

    [
        [".",".",".",".","5",".",".","1","."],
        [".","4",".","3",".",".",".",".","."],
        [".",".",".",".",".","3",".",".","1"],
        ["8",".",".",".",".",".",".","2","."],
        [".",".","2",".","7",".",".",".","."],
        [".","1","5",".",".",".",".",".","."],
        [".",".",".",".",".","2",".",".","."],
        [".","2",".","9",".",".",".",".","."],
        [".",".","4",".",".",".",".",".","."]]
    s = Solution()
    a = s.isValidSudoku(input1)
    b = s.isValidSudoku(input2)
    c = s.isValidSudoku(input3)
    
    print(a, b, c)
    pass
