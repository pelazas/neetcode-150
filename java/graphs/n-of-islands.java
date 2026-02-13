class Solution {
    public int numIslands(char[][] grid) {
        int n_islands = 0;
        for (int r = 0; r< grid.length;r++){
            for (int c= 0; c < grid[0].length;c++){
                if (grid[r][c] == '1'){
                    n_islands++;
                    dfs(r,c, grid);
                }
            }
        }
        return n_islands;
    }

    private void dfs(int row, int col, char[][] grid){
        if (row < 0 || col < 0 || row >= grid.length || col >= grid[0].length || grid[row][col] == '0') {
            return;
        }
        // set grid[r][c] to 0
        grid[row][col] = '0';
        // call dfs on adjacent cells - keep in mind boundaries
        dfs(row - 1, col, grid); // Up
        dfs(row + 1, col, grid); // Down
        dfs(row, col - 1, grid); // Left
        dfs(row, col + 1, grid); // Right

    }
}