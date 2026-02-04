class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):

                val = board[r][c]
                if val == ".":
                    continue

                square = (r//3, c//3)

                # check
                if val in rows[r] or val in cols[c] or val in squares[square]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                squares[square].add(val)

        return True
        