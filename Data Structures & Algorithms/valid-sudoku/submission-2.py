class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowDict = collections.defaultdict(set)
        colDict = collections.defaultdict(set)
        boxDict = collections.defaultdict(set)


        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if col == ".":
                    continue

                if col in rowDict[i]:
                    return False
                else:
                    rowDict[i].add(col)

                if col in colDict[j]:
                    return False
                else:
                    colDict[j].add(col)

                if col in boxDict[(i//3, j//3)]:
                    return False
                else:
                    boxDict[(i//3, j//3)].add(col)

        return True

                