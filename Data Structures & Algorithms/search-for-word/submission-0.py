class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = []
        m = len(board)
        n = len(board[0])

        def backtrack(row, col, i):
            if i == len(word):
                return True

            if row < 0 or row >= m or col < 0 or col >= n or board[row][col] != word[i]:
                return False
            
            temp = board[row][col]
            board[row][col] = "#"

            found = (
                backtrack(row + 1, col, i + 1) or
                backtrack(row, col + 1, i + 1) or
                backtrack(row - 1, col, i + 1) or
                backtrack(row, col - 1, i + 1)
                ) 

            board[row][col] = temp
            return found

        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        return False

            

            

            