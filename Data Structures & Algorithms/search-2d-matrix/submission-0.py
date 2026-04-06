class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = (len(matrix)-1) // 2
        col = 0

        def checkRow(col, row):
            while col < len(matrix[row]):
                if matrix[row][col] == target:
                    return True
                col += 1
            return False

        while 0 <= row < len(matrix):
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                if row+1 > len(matrix)-1:
                    return checkRow(col, row)
                elif matrix[row+1][col] > target:
                    return checkRow(col, row)

                else:
                    row += 1
                    col = 0
            else:
                if row-1 < 0:
                    return checkRow(col, row)
                else:
                    row -= 1
                    col = 0
                
                



