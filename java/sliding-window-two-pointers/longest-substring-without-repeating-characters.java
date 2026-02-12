class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character,Integer> seen_map = new HashMap<>();
        int l = 0;
        int result = 0;
        for(int r = 0; r< s.length(); r++){
            if((seen_map.containsKey(s.charAt(r))) && (seen_map.get(s.charAt(r)) >= l)){
                l = seen_map.get(s.charAt(r)) + 1;
            }
            seen_map.put(s.charAt(r), r);
            
            result = Math.max(r-l +1, result);
        }

        return result;
    }
}