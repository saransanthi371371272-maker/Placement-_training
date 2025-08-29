
class GfG {
  
  	
    static int longestSubarray(int[] arr, int k) {
        int res = 0;

        for (int i = 0; i < arr.length; i++) {
            
           
            int sum = 0;
            for (int j = i; j < arr.length; j++) {
                sum += arr[j];
              
               
                if (sum == k) {
                  
                   
                    int subLen = j - i + 1;
                    res = Math.max(res, subLen);
                }
            }
        }

        return res;
    }

    public static void main(String[] args) {
        int[] arr = {10, 5, 2, 7, 1, -10};
        int k = 15;
        System.out.println(longestSubarray(arr, k));
    }
}
