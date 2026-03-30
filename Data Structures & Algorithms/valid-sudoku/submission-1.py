class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row:
                    return False
                row.add(board[i][j])

        for j in range(9):
            col = set()
            for i in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in col:
                    return False
                col.add(board[i][j])


        for i in range(9):
            start_r = i // 3 * 3
            start_c = i % 3 * 3
            box = set()
            for j in range(start_r, start_r + 3):
                for k in range(start_c, start_c + 3):
                    if board[j][k] == ".":
                        continue
                    if board[j][k] in box:
                        return False
                    box.add(board[j][k])

        return True
                
