class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        checkBox = defaultdict(list)
        checkRow = defaultdict(list)
        checkCol = defaultdict(list)

        for row in range(len(board)):

            for col in range(len(board[row])):
                if board[row][col] == '.':
                    continue

                if board[row][col] in checkCol[col]:
                    return False

                if board[row][col] in checkBox[(row // 3, col // 3)]:
                    return False

                if board[row][col] in checkRow[row]:
                    return False

            

                checkCol[col].append(board[row][col])
                checkBox[(row // 3, col // 3)].append(board[row][col])
                checkRow[row].append(board[row][col])


        return True
            
