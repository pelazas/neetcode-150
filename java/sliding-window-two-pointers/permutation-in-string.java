class Solution {
    public boolean checkInclusion(String s1, String s2) {
        HashMap<Character, Integer> freq_map = new HashMap(); // key=char, value=frequency
        for(int i = 0; i<s1.length(); i++){
            freq_map.put(s1.charAt(i), freq_map.getOrDefault(s1.charAt(i), 0) + 1);
        }
        int l = 0;
        HashMap<Character, Integer> window = new HashMap();
        // iterate with a window of size len(s1) through s2
        for(int r = 0; r < s2.length(); r++){
            window.put(s2.charAt(r), window.getOrDefault(s2.charAt(r),0)+1);
            if(r - l +1 > s1.length()){
                char leftChar = s2.charAt(l);
                window.put(leftChar, window.get(leftChar)-1);
                if (window.get(leftChar) == 0){ window.remove(leftChar);}
                l++;

            }
            if (window.equals(freq_map)){
                return true;
            }

        }

        return false;
    }
}