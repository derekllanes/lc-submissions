class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colCheck = [set() for _ in range(len(board))]
        rowCheck = [set() for _ in range(len(board[0]))]
        boxCheck = collections.defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == '.':
                    continue 

                if board[row][col] in colCheck[col]:
                    return False
                
                if board[row][col] in rowCheck[row]:
                    return False

                if board[row][col] in boxCheck[(row // 3, col // 3)]:
                    return False

                colCheck[col].add(board[row][col])
                rowCheck[row].add(board[row][col])
                boxCheck[(row // 3, col // 3)].add(board[row][col])

        return True


