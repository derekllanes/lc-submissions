class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bot = len(matrix)-1

        while top <= bot:
            m = top + (bot - top) // 2

            if target > matrix[m][-1]:
                top = m+1
            elif matrix[m][0] > target:
                bot = m-1
            else:
                break

        if not top <= bot:
            return False

        l = 0
        r = len(matrix[0])-1

        while l <= r:
            mm = l + (r - l) // 2

            if target > matrix[m][mm]:
                l = mm+1
            elif target < matrix[m][mm]:
                r = mm-1
            else:
                return True

        return False
            