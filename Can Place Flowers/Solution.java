class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int size = flowerbed.length;
        int i = 0;
        while ((n > 0) && (i < size)){
            if(i == 0 || flowerbed[i - 1] == 0){
                if((i == size-1) ||flowerbed[i + 1] == 0){
                    if(flowerbed[i] == 0){
                        flowerbed[i] = 1;
                        n--;
                    }
                    i = i+2;
                } else{
                    i = i+3;
                }

            } else {
                i = i+1;
            }
        }
        boolean output = !(n > 0);
        return output;
    }
}