class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = collections.defaultdict(set)
        colMap = collections.defaultdict(set)
        squareMap = collections.defaultdict(set)

        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num == ".":
                    continue

                if num in rowMap[i]:
                    return False

                if num in colMap[j]:
                    return False

                if num in squareMap[(i//3, j//3)]:
                    return False

                rowMap[i].add(num)
                colMap[j].add(num)
                squareMap[(i//3,j//3)].add(num)

        return True
