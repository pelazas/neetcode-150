import java.util.*;

public class RelayTowers {

    /**
     * Determines the maximum storm level at which data can still be transmitted.
     *
     * @param x          Array of x-coordinates for the towers.
     * @param heights    Array of heights corresponding to x[i].
     * @param width      The x-coordinate of the destination office (Start is 0).
     * @param maxJump    The maximum horizontal distance for a single jump.
     * @param maxEnergy  The total energy budget (sum of squared jump distances).
     * @return           The maximum storm height.
     */
    public static int solve(int[] x, int[] heights, int width, int maxJump, int maxEnergy) {
        // Collect all possible candidate heights for the storm.
        Set<Integer> distinctHeights = new HashSet<>();
        distinctHeights.add(0);
        for (int h : heights) {
            distinctHeights.add(h);
        }
        
        // Convert to a sorted list for Binary Search
        List<Integer> sortedHeights = new ArrayList<>(distinctHeights);
        Collections.sort(sortedHeights);

        // 2. Combine x and heights into a list of Tower objects for easier filtering
        int n = x.length;
        List<Tower> allTowers = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            allTowers.add(new Tower(x[i], heights[i]));
        }

        // Binary Search for the maximum valid storm level
        int low = 0;
        int high = sortedHeights.size() - 1;
        int maxValidStorm = 0;

        while (low <= high) {
            int midIdx = low + (high - low) / 2;
            int stormLevel = sortedHeights.get(midIdx);

            if (canReach(stormLevel, allTowers, width, maxJump, maxEnergy)) {
                maxValidStorm = stormLevel;
                low = midIdx + 1; // Try a higher storm level
            } else {
                high = midIdx - 1; // lower the storm
            }
        }

        return maxValidStorm;
    }

    private static boolean canReach(int stormLevel, List<Tower> allTowers, int width, int maxJump, int maxEnergy) {
        List<Integer> activePoints = new ArrayList<>();
        
        activePoints.add(0);
        
        for (Tower t : allTowers) {
            if (t.height >= stormLevel) {
                activePoints.add(t.x);
            }
        }
        
        activePoints.add(width);

        Collections.sort(activePoints);

        int m = activePoints.size();
        long[] dp = new long[m]; 
        Arrays.fill(dp, Long.MAX_VALUE);
        
        dp[0] = 0; 

        for (int i = 0; i < m; i++) {
            if (dp[i] == Long.MAX_VALUE) continue;

            for (int j = i + 1; j < m; j++) {
                int dist = activePoints.get(j) - activePoints.get(i);

                if (dist > maxJump) break;

                long cost = (long) dist * dist;
                
                if (dp[i] + cost <= maxEnergy) {
                    if (dp[i] + cost < dp[j]) {
                        dp[j] = dp[i] + cost;
                    }
                }
            }
        }

        return dp[m - 1] <= maxEnergy;
    }

    // Helper class to store tower data
    static class Tower {
        int x;
        int height;

        public Tower(int x, int height) {
            this.x = x;
            this.height = height;
        }
    }

    // --- Main method for testing ---
    public static void main(String[] args) {
        int[] x = {5, 10, 15};
        int[] heights = {10, 5, 12};
        int width = 20;
        int maxJump = 10;
        int maxEnergy = 200;

        int result = solve(x, heights, width, maxJump, maxEnergy);
        System.out.println("Max Storm Level: " + result); 
    }
}