class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(9):
            for j in range(9):
                v = board[i][j]

                if v == ".":
                    continue

                b = (i // 3, j // 3)
                if v in rows[i] or v in columns[j] or v in boxes[b]:
                    return False

                rows[i].add(v)
                columns[j].add(v)
                boxes[b].add(v)

        return True