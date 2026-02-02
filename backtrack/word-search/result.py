class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        rows, cols = len(board), len(board[0])

        def backtrack(r,c,index):
            if index == len(word):
                return True
            
            #check out of bounds or wrong letter or visited
            if (r<0 or c<0 or r>=rows or c >= cols or word[index] != board[r][c] or (r,c) in path):
                return False
            
            path.add((r,c))

            #explore neighbours
            res = (
                backtrack(r+1,c,index+1) or
                backtrack(r-1,c,index+1) or
                backtrack(r,c+1,index+1) or
                backtrack(r,c-1,index+1)
            )

            path.remove((r,c))

            return res

        #find starting point
        for i in range(rows):
            for j in range(cols):
                if backtrack(i,j,0):
                    return True
        return False