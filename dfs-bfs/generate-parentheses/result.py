class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #dfs
        result = []
        max_length = n * 2

        def dfs(open_count, close_count, str):
            if len(str) == max_length:
                result.append(str)
                return
            if open_count < n:
                dfs(open_count+1, close_count, str+ "(")
            if close_count < open_count:
                dfs(open_count, close_count+1, str+")")
        
        dfs(0,0,"")
        return result

        