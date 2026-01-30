class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue = deque()
        if image[sr][sc] == color:
            return image

        original_color = image[sr][sc]
        image[sr][sc] = color
        queue.append((sr,sc))

        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        while queue:
            r,c = queue.popleft()
            for direction in directions:
                n_r,n_c = r+direction[0], c+direction[1]
                if 0 <= n_r < len(image) and 0 <= n_c < len(image[0]) and image[n_r][n_c] == original_color:
                    image[n_r][n_c] = color
                    queue.append((n_r,n_c))
        return image

