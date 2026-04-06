class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = collections.defaultdict(set)
        colSet = collections.defaultdict(set)
        boxSet = collections.defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if (board[row][col] in rowSet[row] 
                    or board[row][col] in colSet[col] 
                    or board[row][col] in boxSet[(row // 3, col // 3)]):
                    return False

                rowSet[row].add(board[row][col])
                colSet[col].add(board[row][col])
                boxSet[(row//3,col//3)].add(board[row][col])


        return True

                