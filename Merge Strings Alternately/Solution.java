class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder output =new StringBuilder();
        int maxval = Math.max(word1.length(), word2.length());

        for(int i = 0; i < maxval; i++){
            if (word1.length() > i){
                output.append(word1.charAt(i));
            }
            if (word2.length() > i){
                output.append(word2.charAt(i));
            }
        }
        return output.toString();

        
    }
}