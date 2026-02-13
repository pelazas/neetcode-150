class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }
        for (int[] edge : prerequisites) {
            graph.get(edge[1]).add(edge[0]); // Course 1 -> Course 0
        }
        // 0 = Unvisited, 1 = Visiting, 2 = Visited
        int[] state = new int[numCourses];

        for (int i = 0; i < numCourses; i++) { // graph might be disconnected
            if (state[i] == 0) {
                if (hasCycle(i, graph, state)) {
                    return false;
                }
            }
        }
        return true;
    }

    private boolean hasCycle(int course, List<List<Integer>> graph, int[] state) {
        if (state[course] == 1) return true; // currently visiting
        if (state[course] == 2) return false; // already visited, no cycle here
        state[course] = 1;

        // Visit all neighbors
        for (int neighbor : graph.get(course)) {
            if (hasCycle(neighbor, graph, state)) {
                return true;
            }
        }

        // Mark as visited
        state[course] = 2;
        return false;
    }
}